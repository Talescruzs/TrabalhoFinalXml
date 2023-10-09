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
        self.validJson = dict()
        self.invalidJson = list()
        self.files=files

        with open(jsonSchemaPath, 'r') as file:
                self.schema = json.load(file)

        self.__validate()

    def __validate(self):
        for currentFile in self.files.jsonFiles:
            with open(self.files.jsonFolder+currentFile, 'r') as file:
                thisJson = json.load(file)
            
            validator = Draft7Validator(self.schema)
            
            if(len(list(validator.iter_errors(thisJson)))==0):
                self.validJson[currentFile]=thisJson
            else:
                self.invalidJson.append(currentFile)

class Search:
    def __init__(self, files:Validator):
        self.validFiles = files.validJson
        self.invalidFiles = files.invalidJson

    def __nameFilesProcessing(self, nameFiles):
        files = list()
        if(nameFiles=="."):
            files = list(self.validFiles.values())
        else:
            names = nameFiles.split(",")
            for name in names:
                files.append(self.validFiles[name])
        return files
    
    def __searchProcessing(self, search):
        research = list()
        if("/" in search):
            research = search.split("/")
        else:
            research.append(search)
        return research
    
    def __treeSearch(self, search, file):
        parsedSearch = file
        flag = 0
        results = list()
        for layer in range(len(search)):
            try:
                parsedSearch = parsedSearch[search[layer]]
            except:
                flag=1
                if(type(parsedSearch)==list):
                    newSearch = list()
                    for a in range(len(search)):
                        if(a>=layer):
                            newSearch.append(search[layer])
                    for division in parsedSearch:
                        results.append(self.__treeSearch(newSearch, division))
                else:
                    pass
        if(flag==0):
            results = parsedSearch
        return results

    def search(self, search:str, nameFiles="."):
        results = list()
        filesSearched = self.__nameFilesProcessing(nameFiles)
        processedSearch = self.__searchProcessing(search)    

        for file in filesSearched:
            results.append(self.__treeSearch(processedSearch, file))
            
        return results

if __name__ == "__main__":
    teste1 = Files("notasFiscais/", "Json/")
    teste2 = Validator(teste1, "schema.json")
    #vProd = valor de produto
    # print(teste2.validJson["nota1.json"]["ns0:nfeProc"]["@xmlns:ns0"])
    teste3 = Search(teste2)
    a=0
    v=0
    for i in range(len(teste3.search("ns0:nfeProc/ns0:NFe/ns0:infNFe/ns0:det/@nItem"))):
        valor = teste3.search("ns0:nfeProc/ns0:NFe/ns0:infNFe/ns0:total/ns0:ICMSTot/ns0:vProd")
        a+=int(teste3.search("ns0:nfeProc/ns0:NFe/ns0:infNFe/ns0:det/@nItem")[i][-1])
        v+=float(valor[i])
    print(a)
    print(v)
    # teste3.search("ns0:nfeProc/ns0:NFe/ns0:infNFe/ns0:det", "nota5.json")
