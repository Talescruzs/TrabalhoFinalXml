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
    tributos1 = files.search("ns0:nfeProc/ns0:NFe/ns0:infNFe/ns0:total/ns0:ICMSTot/ns0:vICMS")
    tributos2 = files.search("ns0:nfeProc/ns0:NFe/ns0:infNFe/ns0:total/ns0:ICMSTot/ns0:vTotTrib")
    totalTributos = dict()
    for k in list(tributos1.keys()):
        totalTributos[k] = str(float(tributos1[k]) + float(tributos2[k]))

    consulta={
        "ISSQN" : issqn,
        "ICMS" : icms,
        "vTributos" : totalTributos,
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

def consulta_d(files: Search):
    vTributos = consulta_b(files)["vTributos"]
    maiorTributos = 0
    notasMaiorTributo = list()
    consulta=dict()
    for k in vTributos:
        if(k!="total"):
            if(float(vTributos[k])>float(maiorTributos)):
                notasMaiorTributo = list([k])
                maiorTributos=vTributos[k]
            elif(float(vTributos[k])==float(maiorTributos)):
                notasMaiorTributo.append(k)
    
    for nota in notasMaiorTributo:
        consulta[nota] = detalhes(files, nota)

    return consulta

if __name__=="__main__":
    teste1 = Files("notasFiscais/", "Json/")
    teste2 = Validator(teste1, "schema.json")
    teste3 = Search(teste2)
    print(consulta_d(teste3))