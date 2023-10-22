from Files import Validator, Files
from Search import Search

def consulta_a(files: Search):
    qtdProdutos=0
    valorProdutos=0
    valores = files.search("ns0:nfeProc/ns0:NFe/ns0:infNFe/ns0:total/ns0:ICMSTot/ns0:vProd")
    for i in range(len(files.search("ns0:nfeProc/ns0:NFe/ns0:infNFe/ns0:det/@nItem"))):
        qtdProdutos+=int(files.search("ns0:nfeProc/ns0:NFe/ns0:infNFe/ns0:det/@nItem")[i][-1])
        valorProdutos+=float(valores[i])
    consulta={
        "qtdProdutos" : qtdProdutos,
        "valorProdutos" : valorProdutos
    }
    return consulta

def consulta_b(files: Search):
    frete=0
    icms=0
    valoresIcms = files.search("ns0:nfeProc/ns0:NFe/ns0:infNFe/ns0:total/ns0:ICMSTot/ns0:vICMS")
    valoresFrete = files.search("ns0:nfeProc/ns0:NFe/ns0:infNFe/ns0:total/ns0:ICMSTot/ns0:vFrete")
    for i in range(len(files.search("ns0:nfeProc/ns0:NFe/ns0:infNFe/ns0:det/@nItem"))):
        icms+=float(valoresIcms[i])
        frete+=float(valoresFrete[i])
    consulta={
        "ISSQN" : 'nada retido',
        "ICMS" : icms,
        "vTributos" : 'apenas o icms',
        "frete" : frete
    }
    return consulta
