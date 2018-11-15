from lxml import etree

# xml_decl = '<?xml version="1.0" encoding="UTF-8"?>'
# mk_doctype = '<!DOCTYPE SYSTEM tei_ha_digipub_ak.dtd>'

my_file = 'edition_bretke_asarie.tei'

parser = etree.XMLParser(dtd_validation=True)
root = etree.parse(my_file, parser).getroot()

# outstr = xml_decl + '\n' + mk_doctype + '\n' + etree.tostring(root, encoding="unicode", pretty_print=True)
# with open(outfile, 'w') as sd:
#     sd.write(outstr)

# TODO: Korrekte Verarbeitung von Unicode überprüfen! - sieht erstmal ganz gut aus...