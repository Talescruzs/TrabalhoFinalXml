from Files import Validator, Files
from Search import Search

def consulta_a(files: Search):
    qtdProdutos=0
    valorProdutos=0
    valorProdutos = files.search("ns0:nfeProc/ns0:NFe/ns0:infNFe/ns0:total/ns0:ICMSTot/ns0:vProd")
    qtdProdutos = files.search("ns0:nfeProc/ns0:NFe/ns0:infNFe/ns0:det/@nItem")
    consulta={
        "qtdProdutos" : qtdProdutos,
        "valorProdutos" : valorProdutos
    }
    return consulta

def consulta_b(files: Search):
    frete=0
    icms=0
    icms = files.search("ns0:nfeProc/ns0:NFe/ns0:infNFe/ns0:total/ns0:ICMSTot/ns0:vICMS")
    frete = files.search("ns0:nfeProc/ns0:NFe/ns0:infNFe/ns0:total/ns0:ICMSTot/ns0:vFrete")
    issqn = files.search("ns0:nfeProc/ns0:NFe/ns0:infNFe/ns0:total/ns0:ISSQNtot/ns0:vISS")
    tributos = files.search("ns0:nfeProc/ns0:NFe/ns0:infNFe/ns0:total/ns0:ICMSTot/ns0:vFrete")
    # tributos = {"total" : 0}
    consulta={
        "ISSQN" : issqn,
        "ICMS" : icms,
        "vTributos" : issqn,
        "frete" : frete
    }
    return consulta

def detalhes(files: Search, file: str):
    nomeProd = files.search("ns0:nfeProc/ns0:NFe/ns0:infNFe/ns0:det/ns0:prod/ns0:xProd")[file]
    nomeRemetente = files.search("ns0:nfeProc/ns0:NFe/ns0:infNFe/ns0:dest/ns0:xNome")[file]
    valorProd = files.search("ns0:nfeProc/ns0:NFe/ns0:infNFe/ns0:det/ns0:prod/ns0:vProd")[file]

    consulta={
        "nomeProd" : nomeProd,
        "nomeRemetente" : nomeRemetente,
        "valorProd" : valorProd
    }

    return consulta

def consulta_c(files: Search):
    precos = files.search("ns0:nfeProc/ns0:NFe/ns0:infNFe/ns0:total/ns0:ICMSTot/ns0:vProd")
    menorPreco = precos["total"]
    notasMenorPreco = list()
    consulta=dict()
    for k in precos:
        if(k!="total"):
            if(float(precos[k])<float(menorPreco)):
                notasMenorPreco = list([k])
                menorPreco=precos[k]
            elif(float(precos[k])==float(menorPreco)):
                notasMenorPreco.append(k)
    
    for nota in notasMenorPreco:
        consulta[nota] = detalhes(files, nota)

    return consulta

if __name__=="__main__":
    teste1 = Files("notasFiscais/", "Json/")
    teste2 = Validator(teste1, "schema.json")
    teste3 = Search(teste2)
    print(consulta_c(teste3))