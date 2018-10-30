from lxml import etree

xml_decl = '<?xml version="1.0" encoding="UTF-8"?>'
mk_doctype = '<!DOCTYPE tei_doctype SYSTEM "tei_ha_digipub_ak.dtd">'

filnom = 'bretke_geb-asarie.tei'
outfile = 'edition_bretke_asarie.tei'

parser = etree.XMLParser(remove_blank_text=True)
root = etree.parse(filnom, parser).getroot()

outstr = xml_decl + '\n' + mk_doctype + '\n' + etree.tostring(root, encoding="unicode", pretty_print=True)
with open(outfile, 'w') as sd:
    sd.write(outstr)

# TODO: Korrekte Verarbeitung von Unicode überprüfen! - sieht erstmal ganz gut aus...