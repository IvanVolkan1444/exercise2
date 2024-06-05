import xml.etree.ElementTree as ET
import xml.dom.minidom

class ResultWriter:
    def __init__(self, filename):
        self.filename = filename

    def prettify(self, elem):
        rough_string = ET.tostring(elem, 'utf-8')
        reparsed = xml.dom.minidom.parseString(rough_string)
        return reparsed.toprettyxml(indent="    ")

    def write_to_xml(self, data):
        root = ET.Element("data")
        for entry in data:
            row = ET.SubElement(root, "row")
            freq_elem = ET.SubElement(row, "freq")
            freq_elem.text = str(entry["freq"])
            lambda_elem = ET.SubElement(row, "lambda")
            lambda_elem.text = str(entry["lambda"])
            rcs_elem = ET.SubElement(row, "rcs")
            rcs_elem.text = str(entry["rcs"])

        with open(self.filename, "w") as f:
            f.write(self.prettify(root))