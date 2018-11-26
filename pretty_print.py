import sys
from lxml import etree

import automate_toks as toks
import characters

xml_decl = '<?xml version="1.0" encoding="UTF-8"?>'
mk_doctype = '<!DOCTYPE TEI SYSTEM "tei_all.dtd">'

infile = 'bretke_geb-asarie.tei'
outfile = 'edition_bretke_asarie.tei'
# outfile = 'test_tok_id.xml'
intermediary = 'bretke_chars_changed.tei'

def process_unicode(text):
    text = characters.use_escapes(text)
    return text

# Datei einlesen:
parser = etree.XMLParser(remove_blank_text=True)
root = etree.parse(infile, parser).getroot()
root = toks.generate_token_id(root)

# gucken, ob wir unicode noch mal anders wollen:
# und in neue Datei schreiben:

outstr = xml_decl + '\n' + mk_doctype + '\n' + etree.tostring(root, encoding="unicode", pretty_print=True)
if len(sys.argv) > 1 and sys.argv[1] == 'escapeUnicode':
    outstr = process_unicode(outstr)
with open(outfile, 'w') as sd:
    sd.write(outstr)

# TODO: Korrekte Verarbeitung von Unicode überprüfen! - sieht erstmal ganz gut aus...