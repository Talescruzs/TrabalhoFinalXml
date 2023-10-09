import xml.etree.ElementTree as ET
import xmltodict, json
import os
from jsonschema import Draft7Validator

class Files:
    def __init__(self, xmlFolderPath:str, jsonFolderPath:str):
        self.xmlFiles = self.__getLocalFiles(xmlFolderPath)
        self.xmlFolder = xmlFolderPath
        self.jsonFolder = jsonFolderPath

        for file in range(len(self.xmlFiles)):
            self.__createJson(self.xmlFiles[file], file)

        self.jsonFiles = self.__getLocalFiles(self.jsonFolder)

    def __getLocalFiles(self, folderPath:str):
        res = list()
        for file_path in os.listdir(folderPath):
            if os.path.isfile(os.path.join(folderPath, file_path)):
                res.append(file_path)
        return res

    def __createJson(self, file:str, index:int):
        xmlFile = self.xmlFolder+file
        xml_tree = ET.parse(xmlFile)
        root = xml_tree.getroot()
        to_string  = ET.tostring(root, encoding='UTF-8', method='xml')
        xml_to_dict = xmltodict.parse(to_string)

        with open("Json/{0}.json".format(file.split(".")[0]), "w",) as json_file:
            json.dump(xml_to_dict, json_file, indent = 2)

class Validator:
    def __init__(self, files:Files, jsonSchemaPath:str):
        self.validJson = list()
        self.invalidJson = list()
        self.files=files

        with open(jsonSchemaPath, 'r') as file:
                self.schema = json.load(file)

        self.__validate()

    def __validate(self):
        print(self.files.xmlFiles)
        print(self.files.jsonFiles)
        print(self.files.xmlFolder)
        print(self.files.jsonFolder)
        for currentFile in self.files.jsonFiles:
            with open(self.files.jsonFolder+currentFile, 'r') as file:
                thisJson = json.load(file)
            
            validator = Draft7Validator(self.schema)
            print(currentFile, ":\n")
            print(list(validator.iter_errors(thisJson)))
            print("\n\n\n")
            
            if(len(list(validator.iter_errors(thisJson)))==0):
                self.validJson.append(currentFile)
            else:
                self.invalidJson.append(currentFile)
        print(self.invalidJson)
        print(self.validJson)

if __name__ == "__main__":
    teste1 = Files("notasFiscais/", "Json/")
    teste2 = Validator(teste1, "schema.json")