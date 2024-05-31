import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """Serialize a dictionary to an XML file."""
    root = ET.Element("data")
    
    for key, value in dictionary.items():
        item = ET.SubElement(root, key)
        item.text = str(value)
    
    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)

def deserialize_from_xml(filename):
    """Deserialize an XML file to a dictionary."""
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        
        dictionary = {}
        for child in root:
            dictionary[child.tag] = child.text
        
        return dictionary
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
        return None
    except ET.ParseError as e:
        print(f"An error occurred while parsing the XML file: {e}")
        return None
