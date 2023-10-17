from flask import Flask, render_template
from Files import Validator, Files
from Search import Search

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("index.html", valores=teste, notasValidas=notasValidas, qtdNotas=len(notasValidas))

@app.route('/consulta-produto')
def consulta_produto():
    return render_template("consulta-produto.html", consulta=consulta)

@app.route('/consulta-b')
def consulta_b():
    return render_template("consulta-b.html", consulta=consulta)

if __name__ == "__main__":
    teste1 = Files("notasFiscais/", "Json/")
    teste2 = Validator(teste1, "schema.json")
    notasValidas = list(teste2.validJson.keys())
    for i in range(len(notasValidas)):
        notasValidas[i] = notasValidas[i].replace(".json", "")
    
    #vProd = valor de produto
    # print(teste2.validJson["nota5.json"]["ns0:nfeProc"]["ns0:NFe"]["ns0:infNFe"]["ns0:det"])
    teste3 = Search(teste2)
    qtdProdutos=0
    valorProdutos=0
    valores = teste3.search("ns0:nfeProc/ns0:NFe/ns0:infNFe/ns0:total/ns0:ICMSTot/ns0:vProd")
    teste = teste3.search("ns0:nfeProc/ns0:NFe/ns0:infNFe/ns0:total/ns0:ICMSTot/ns0:vProd", "nota1.json")
    for i in range(len(teste3.search("ns0:nfeProc/ns0:NFe/ns0:infNFe/ns0:det/@nItem"))):
        qtdProdutos+=int(teste3.search("ns0:nfeProc/ns0:NFe/ns0:infNFe/ns0:det/@nItem")[i][-1])
        valorProdutos+=float(valores[i])
    consulta={
        "qtdProdutos" : qtdProdutos,
        "valorProdutos" : valorProdutos
    }
        
    app.run(debug=True)