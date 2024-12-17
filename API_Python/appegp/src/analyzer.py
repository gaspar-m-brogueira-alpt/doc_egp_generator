import zipfile
import xml.etree.ElementTree as ET


import zipfile
import re


def analyze_egp_file(file_path):
    tables = []
    table_pattern = re.compile(
        r'\bFROM\s+(dcisas_k|dme_prd)\.\w+', re.IGNORECASE)

    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        for file in zip_ref.namelist():
            if file.endswith('.log'):
                with zip_ref.open(file) as log_file:
                    for line in log_file:
                        print(line)
                        line = line.decode('utf-8')
                        # matches = table_pattern.findall(line)
                        if "FROM" in line:
                            tokens = line.split(" ")
                            print(tokens)
                        # print(matches)
                        # for match in matches:
                        #    tables.append(match)
    return list(set(tables))  # Remove duplicates
