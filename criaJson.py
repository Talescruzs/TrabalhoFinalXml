import xmltodict, json
from Files import Files, Validator
from Search import Search


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
    # teste3.search("ns0:nfeProc/ns0:NFe/ns0:infNFe/ns0:det", "nota5.json")
