from Files import Validator, Files

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
    # print(teste2.validJson["nota5.json"]["ns0:nfeProc"]["ns0:NFe"]["ns0:infNFe"]["ns0:det"])
    teste3 = Search(teste2)
    a=0
    v=0
    for i in range(len(teste3.search("ns0:nfeProc/ns0:NFe/ns0:infNFe/ns0:det/@nItem"))):
        valor = teste3.search("ns0:nfeProc/ns0:NFe/ns0:infNFe/ns0:total/ns0:ICMSTot/ns0:vProd")
        a+=int(teste3.search("ns0:nfeProc/ns0:NFe/ns0:infNFe/ns0:det/@nItem")[i][-1])
        v+=float(valor[i])
    print(a)
    print(v)