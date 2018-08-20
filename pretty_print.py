from lxml import etree

xml_decl = '<?xml version="1.0" encoding="UTF-8"?>'

filnom = 'bretke_geb-asarie.tei'
outfile = 'edtion_bretke_asarie.tei'

parser = etree.XMLParser(remove_blank_text=True, encoding="unicode")
root = etree.parse(filnom, parser).getroot()

outstr = xml_decl + '\n' + etree.tostring(root, encoding="unicode", pretty_print=True)
with open(outfile, 'w') as sd:
    sd.write(outstr)

# TODO: Korrekte Verarbeitung von Unicode überprüfen!