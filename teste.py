from flask import Flask, render_template
from Files import Validator, Files
from Search import Search

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("index.html", a=a, v=v)

@app.route('/teste')
def teste():
    return render_template("teste.html")

@app.route('/about/')
def about():
    return '<h3>This is a Flask .</h3>'

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
    app.run(debug=True)