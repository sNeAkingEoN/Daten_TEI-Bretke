from lxml import etree
import re, os.path

infile = os.path.normpath('bretke_geb-asarie.tei')

re_token_id = re.compile(r'tok-23([45])([rv])(\d\d?)-(\d\d\d)')

# ns = 'http://www.tei-c.org/ns/1.0'
ns = 'tei'

parser = etree.XMLParser(remove_blank_text=True)
root = etree.parse(infile, parser).getroot()
# print(root[0].tag)

# path = "//*[local-name()='w']"
# tokenlist = root.xpath(path)

tei_ns = 'http://www.tei-c.org/ns/1.0'
tei = '{'+ tei_ns + '}'
xml_ns = 'http://www.w3.org/XML/1998/namespace'
xml = '{' + xml_ns + '}'

nss = {'tei': 'http://www.tei-c.org/ns/1.0', 'xml': 'http://www.w3.org/XML/1998/namespace'}

tokenlist = root.xpath('//tei:div[@type="edited_text"]//tei:w|//tei:div[@type="edited_text"]//tei:pc|//tei:div[@type="edited_text"]//tei:lb|//tei:div[@type="edited_text"]//tei:pb', namespaces=nss) 
# tokenlist = root.xpath('//tei:div[@type="edited_text"]//tei:w', namespaces=nss) # so geht's


# compl_list = tokenlist + root.xpath('//tei:div[@type="edited_text"]//tei:lb', namespaces=nss)
# >>> r = doc.xpath('/x:foo/b:bar',
# ...               namespaces={'x': 'http://codespeak.net/ns/test1',
# ...                           'b': 'http://codespeak.net/ns/test2'})

print(tokenlist[0].tag)
print(len(tokenlist))

# generiere automatisch token-id :):
linenr = 0
tok_count = 0
page_name = ''
for token in tokenlist: 
    if token.tag == '{}w'.format(tei): 
        if '{}id'.format(xml) in token.attrib:
            res = re_token_id.search(token.attrib['{}id'.format(xml)])
            if res:
                tok_count = int(res.group(4))
            else:
                print("falsches token?")
        else:
            tok_count += 1
            token.set('{}id'.format(xml), 'tok-{}{:0>2}-{:0>3}'.format(page_name, linenr, tok_count)) 
    #     print(tok_count)
    # print(token.text)
    if token.tag == '{}lb'.format(tei):
        linenr = token.attrib['n']
        print("line", linenr)
    if token.tag == '{}pb'.format(tei):
        # print("page number gefunden!")
        if 'n' in token.attrib:
            print("ja!")
            page_name = token.attrib['n']
            print("page_name", page_name)
            

outstr = etree.tostring(root, encoding='unicode', pretty_print=True)

with open("test_tok_id.xml", 'w') as sd:
    sd.write(outstr)
