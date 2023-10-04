import xml.etree.ElementTree as ET
import xmltodict, json
import os
from jsonschema import Draft7Validator

class Json:
    def __init__(self, xmlFolderPath:str, jsonSchemaPath:str):
        self.__defFiles(xmlFolderPath)

        for file in range(len(self.res)):
            self.__defJson(xmlFolderPath, self.res[file], file)
            # self.validate(jsonSchemaPath)

    def __defFiles(self, xmlFolderPath:str):
        dir_path = xmlFolderPath

        self.res = []

        for file_path in os.listdir(dir_path):
            if os.path.isfile(os.path.join(dir_path, file_path)):
                self.res.append(file_path)

    def __defJson(self, xmlFolderPath:str, file:str, index:int):

        xml_tree = ET.parse(xmlFolderPath+file)
        root = xml_tree.getroot()
        to_string  = ET.tostring(root, encoding='UTF-8', method='xml')
        xml_to_dict = xmltodict.parse(to_string)

        with open("Json/json_data{0}.json".format(index+1), "w",) as json_file:
            json.dump(xml_to_dict, json_file, indent = 2)

        print(root)
        # self.jsonFile = json.dumps(obj)
        # print(self.jsonFile+"\n\n\n\n")
        

    def validate(self, jsonSchemaPath):
        with open(jsonSchemaPath, 'r') as file:
            schema = json.load(file)
        validator = Draft7Validator(schema)
        print(list(validator.iter_errors(self.jsonFile)))


if __name__ == "__main__":
    teste = Json("notasFiscais/", "schema.json")