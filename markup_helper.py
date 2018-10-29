from lxml import etree
import os.path

infile = os.path.normpath("bretke_geb-asarie.tei")
outfile = "list_of_elements.txt"

root = etree.parse(infile).getroot()
elems = root.findall('.//')

print(len(elems))

tags = []
outstring = ""

for elem in elems:
    if elem.tag:
        tags.append(elem.tag)

tags = set(tags)

for tag in tags:
    outstring = outstring + '\n' + str(tag)
    path = './/' + tag
    atts = []
    instances = root.findall(path)
    for inst in instances:
        if inst.attrib:
            for ar in inst.attrib.keys():
                atts.append(ar)
    atts = set(atts)
    if atts:
        outstring = outstring + ' : '
    for att in atts:
        outstring = outstring + att + ' | '
    

with open(outfile, 'w') as sd:
    sd.write(outstring)

