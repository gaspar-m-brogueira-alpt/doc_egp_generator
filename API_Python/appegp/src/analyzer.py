import zipfile
import xml.etree.ElementTree as ET


def analyze_egp_file(file_path):
    tables = []
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        for file in zip_ref.namelist():
            if file.endswith('.xml'):
                with zip_ref.open(file) as xml_file:
                    tree = ET.parse(xml_file)
                    root = tree.getroot()
                    for elem in root.iter():
                        if elem.tag == 'Table' and ('dcisas_k' in elem.text or 'dme_prd' in elem.text):
                            tables.append(elem.text)
    return tables
