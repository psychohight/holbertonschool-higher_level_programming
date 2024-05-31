import json

def serialize_and_save_to_file(data, filename):
    """
    Serialize the given Python dictionary to a JSON file.
    
    data: A Python Dictionary
    filename: The filename 
    """
    with open(filename, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

def load_and_deserialize(filename):
    """
    Load data from a JSON file and deserialize it to a Python dictionary.
    
    filename: The filename
    return: A Python dictionary
    """
    with open(filename, 'r', encoding='utf-8') as json_file:
        return json.load(json_file)
