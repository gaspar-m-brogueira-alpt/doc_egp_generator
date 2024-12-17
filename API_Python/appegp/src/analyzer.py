import zipfile
import xml.etree.ElementTree as ET


import zipfile
import re


def analyze_egp_file(file_path):
    tables = []

    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        for file in zip_ref.namelist():
            if file.endswith('.log'):
                with zip_ref.open(file) as log_file:
                    for line in log_file:
                        line = line.decode('utf-8')
                        if "FROM" in line:
                            tokens = line.split(" ")
                            for token in tokens:
                                if "FROM" in token:
                                    next = tokens[tokens.index(token) + 1]
                                    if "DCISAS_K." in line or "DME_PRD." in line:
                                        tables.append(next)

    return list(set(tables))  # Remove duplicates
