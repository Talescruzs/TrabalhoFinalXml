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
        for layer in search:
            try:
                parsedSearch = parsedSearch[layer]
            except:
                if(type(parsedSearch)==list):
                    newSearch = list()
                    for a in parsedSearch:
                        newSearch.append(a[layer])
                    parsedSearch = newSearch
                else:
                    pass

        return parsedSearch

    def search(self, search:str, nameFiles="."):
        results = dict()
        filesToSearch = self.__nameFilesProcessing(nameFiles)
        processedSearch = self.__searchProcessing(search)  
        total = 0

        for file in filesToSearch:
            results[file] = self.__treeSearch(processedSearch, file)
            if(type(results[file])==dict):
                results[file] = '0'

        for k in results:
            try:
                total+=float(results[k])
            except:
                if(type(results[k])==list):
                    try:
                        for a in results[k]:
                            total+=float(a)
                    except:
                        pass
                        
        results["total"]=str(total)
        return results

if __name__ == "__main__":
    teste1 = Files("notasFiscais/", "Json/")
    teste2 = Validator(teste1, "schema.json")
    teste3 = Search(teste2)
    precos = teste3.search("ns0:nfeProc/ns0:NFe/ns0:infNFe/ns0:det/ns0:prod/ns0:vProd")
    print(precos)