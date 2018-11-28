import sys
from lxml import etree

import automate_toks as toks
import characters

xml_decl = '<?xml version="1.0" encoding="UTF-8"?>'
mk_doctype = '<!DOCTYPE TEI SYSTEM "tei_all.dtd">'

nss = {'tei': 'http://www.tei-c.org/ns/1.0', 'xml': 'http://www.w3.org/XML/1998/namespace'}

infile = 'bretke_geb-asarie.tei'
outfile = 'edition_bretke_asarie.tei'
# outfile = 'test_tok_id.xml'
intermediary = 'bretke_chars_changed.tei'

def process_unicode(text):
    text = characters.use_escapes(text)
    return text

def automate_lemmas(root): # muss noch getestet werden
    elements = root.xpath('//tei:w', namespaces=nss)
    print(root.tag)
    print('Wörter:', len(elements))
    for element in elements:
        if not len(element):
            text = element.text
        else:
            text = element[0].text
        if text == 'ir' or text == 'Ir':
            element.set('lemma', 'ir')
            element.set('pos', 'cnj.')
            element.set('msd', '--')
        elif text == 'tawa':
            element.set('lemma', 'tavo')
            element.set('pos', 'prn.')
            element.set('msd', '--')
        elif text == 'iog':
            element.set('lemma', 'jog')
            element.set('pos', 'cnj.')
            element.set('msd', '--')
    return root

# Datei einlesen:
parser = etree.XMLParser(remove_blank_text=True)
root = etree.parse(infile, parser).getroot()
root = automate_lemmas(root)
root = toks.generate_token_id(root)

# gucken, ob wir unicode noch mal anders wollen:
# und in neue Datei schreiben:

outstr = xml_decl + '\n' + mk_doctype + '\n' + etree.tostring(root, encoding="unicode", pretty_print=True)
if len(sys.argv) > 1 and sys.argv[1] == 'escapeUnicode':
    outstr = process_unicode(outstr)
with open(outfile, 'w') as sd:
    sd.write(outstr)

# TODO: Korrekte Verarbeitung von Unicode überprüfen! - sieht erstmal ganz gut aus...