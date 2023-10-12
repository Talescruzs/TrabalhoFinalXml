import xmltodict, json
from Files import Files, Validator
from Search import Search


if __name__ == "__main__":
    # teste1 = Files("notasFiscais/", "Json/")
    # teste2 = Validator(teste1, "schema.json")
    # #vProd = valor de produto
    # # print(teste2.validJson["nota5.json"]["ns0:nfeProc"]["ns0:NFe"]["ns0:infNFe"]["ns0:det"])
    # teste3 = Search(teste2)
    # a=0

    # for i in teste3.search("ns0:nfeProc/ns0:NFe/ns0:infNFe/ns0:det/@nItem"):
    #     a+=int(i[-1])
    # print("Total de itens:")
    # print(a)

    # for i in teste3.search("ns0:nfeProc/ns0:NFe/ns0:infNFe/ns0:total/ns0:ICMSTot/ns0:vProd"):
    #     a+=float(i)
    # print("Preço total:")
    # print(a, "\n")

    # teste3.search("ns0:nfeProc/ns0:NFe/ns0:infNFe/ns0:det", "nota5.json")

    teste1 = Files("notasFiscais/", "Json/")
    teste2 = Validator(teste1, "schemaTeste.json")
    #vProd = valor de produto
    # print(teste2.validJson["nota5.json"]["ns0:nfeProc"]["ns0:NFe"]["ns0:infNFe"]["ns0:det"])
    teste3 = Search(teste2)
    print(teste3.search("a/b/d"))
    print(teste3.validFiles["notaTotalmenteVerdadeira.json"]["a"])
