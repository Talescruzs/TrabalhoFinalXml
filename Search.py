from Files import Validator, Files

class Search:
    def __init__(self, files:Validator):
        self.validFiles = files.validJson

    def __nameFilesProcessing(self, nameFiles):
        files = list()
        if(nameFiles=="."):
            files = list(self.validFiles.keys())
        else:
            files = nameFiles.split(",")
        return files
    
    def __searchProcessing(self, search):
        research = list()
        if("/" in search):
            research = search.split("/")
        else:
            research.append(search)
        return research
    
    def __treeSearch(self, search, file):
        parsedSearch = self.validFiles[file]
        flag = 0
        results = dict()
        for layer in range(len(search)):
            try:
                parsedSearch = parsedSearch[search[layer]]
            except:
                if(type(parsedSearch)==list):
                    newSearch = list()
                    for a in parsedSearch:
                        parsedSearch = a[search[layer]]
                else:
                    pass
        results = parsedSearch

        return results

    def search(self, search:str, nameFiles="."):
        results = dict()
        filesSearched = self.__nameFilesProcessing(nameFiles)
        processedSearch = self.__searchProcessing(search)  
        total = 0

        for file in filesSearched:
            results[file] = self.__treeSearch(processedSearch, file)
        for k in results:
            try:
                total+=float(results[k])
            except:
                pass
        results["total"]=str(total)
        return results

if __name__ == "__main__":
    teste1 = Files("notasFiscais/", "Json/")
    teste2 = Validator(teste1, "schema.json")
    teste3 = Search(teste2)
    # a=0
    # v=0
    # for i in range(len(teste3.search("ns0:nfeProc/ns0:NFe/ns0:infNFe/ns0:det/@nItem"))):
    #     valor = teste3.search("ns0:nfeProc/ns0:NFe/ns0:infNFe/ns0:total/ns0:ICMSTot/ns0:vProd")
    #     a+=int(teste3.search("ns0:nfeProc/ns0:NFe/ns0:infNFe/ns0:det/@nItem")[i][-1])
    #     v+=float(valor[i])
    # print(a)
    # print(v)
    print(teste3.search("ns0:nfeProc/ns0:NFe/ns0:infNFe/ns0:total/ns0:ICMSTot/ns0:vICMS"))