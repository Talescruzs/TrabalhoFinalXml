from Files import Validator, Files
from Search import Search

def geralSearch(files: Search):
    qtdProdutos=0
    valorProdutos=0
    valorProdutos = files.search("ns0:nfeProc/ns0:NFe/ns0:infNFe/ns0:total/ns0:ICMSTot/ns0:vProd")
    qtdProdutos = files.search("ns0:nfeProc/ns0:NFe/ns0:infNFe/ns0:det/@nItem")
    icms = files.search("ns0:nfeProc/ns0:NFe/ns0:infNFe/ns0:total/ns0:ICMSTot/ns0:vICMS")
    frete = files.search("ns0:nfeProc/ns0:NFe/ns0:infNFe/ns0:total/ns0:ICMSTot/ns0:vFrete")
    issqn = files.search("ns0:nfeProc/ns0:NFe/ns0:infNFe/ns0:total/ns0:ISSQNtot/ns0:vISS")
    icms = files.search("ns0:nfeProc/ns0:NFe/ns0:infNFe/ns0:total/ns0:ICMSTot/ns0:vICMS")
    ipi = files.search("ns0:nfeProc/ns0:NFe/ns0:infNFe/ns0:total/ns0:ICMSTot/ns0:vIPI")
    pis = files.search("ns0:nfeProc/ns0:NFe/ns0:infNFe/ns0:total/ns0:ICMSTot/ns0:vPIS")
    cofins = files.search("ns0:nfeProc/ns0:NFe/ns0:infNFe/ns0:total/ns0:ICMSTot/ns0:vCOFINS")
    tributos = files.search("ns0:nfeProc/ns0:NFe/ns0:infNFe/ns0:total/ns0:ICMSTot/ns0:vTotTrib")

    totalTributos = dict()

    for k in list(icms.keys()):
        if float(tributos[k])==0:
            totalTributos[k] = str(round(float(icms[k])+float(ipi[k])+float(pis[k])+float(cofins[k]), 2))
        else:
            totalTributos[k] = tributos[k]

    consulta={
        "qtdProdutos" : qtdProdutos,
        "valorProdutos" : valorProdutos,
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
    emissao = files.search("ns0:nfeProc/ns0:NFe/ns0:infNFe/ns0:ide/ns0:dEmi")[file]

    consulta={
        "nomeProd" : nomeProd,
        "nomeRemetente" : nomeRemetente,
        "valorProd" : valorProd,
        "emissao" : emissao
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

def detalhesNota(files: Search, file: str, vImposto:str):
    valorProdutos = files.search("ns0:nfeProc/ns0:NFe/ns0:infNFe/ns0:total/ns0:ICMSTot/ns0:vProd")[file]
    qtdProdutos = files.search("ns0:nfeProc/ns0:NFe/ns0:infNFe/ns0:det/@nItem")[file]
    nomeRemetente = files.search("ns0:nfeProc/ns0:NFe/ns0:infNFe/ns0:dest/ns0:xNome")[file]
    emissao = files.search("ns0:nfeProc/ns0:NFe/ns0:infNFe/ns0:ide/ns0:dEmi")[file]

    consulta={
        "valorProdutos" : valorProdutos,
        "qtdProdutos" : qtdProdutos,
        "nomeRemetente" : nomeRemetente,
        "VImposto" : vImposto,
        "emissao" : emissao
    }

    return consulta

def consulta_d(files: Search):
    vTributos = geralSearch(files)["vTributos"]
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
        consulta[nota] = detalhesNota(files, nota, maiorTributos)


    return consulta

if __name__=="__main__":
    teste1 = Files("notasFiscais/", "Json/")
    teste2 = Validator(teste1, "schema.json")
    teste3 = Search(teste2)
    print(consulta_d(teste3))