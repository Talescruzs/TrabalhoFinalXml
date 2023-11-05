from flask import Flask, render_template
from Files import Validator, Files
from Search import Search
import consultas

app = Flask(__name__)

@app.route('/')
def index():
    return render_template(
        "index.html", valores=notasValidas, 
        notasValidas=notasValidas, qtdNotas=len(notasValidas), 
        geralSearch=geralSearch,
        consulta_c=consulta_c, consulta_d=consulta_d,
        qtdMenor=len(consulta_c.values()), notasMenor=list(consulta_c.keys()),
        qtdMaior=len(consulta_d.values()), notasMaior=list(consulta_d.keys()))

@app.route('/notas/<name>')
def notas(name):
    return render_template(
        "nota.html", notasValidas=notasValidas, 
        qtdNotas=len(notasValidas),
        qtdProdutos=consultas.consulta_d(teste3, name+".json"),
        name=name,
        detalhes=consultas.detalhes(teste3, name+".json")
        )

if __name__ == "__main__":
    teste1 = Files("notasFiscais/", "Json/")
    teste2 = Validator(teste1, "schema.json")

    
    #vProd = valor de produto
    # print(teste2.validJson["nota5.json"]["ns0:nfeProc"]["ns0:NFe"]["ns0:infNFe"]["ns0:det"])
    teste3 = Search(teste2)
    notasValidas = list(teste3.validFiles.keys())
    for i in range(len(notasValidas)):
        notasValidas[i] = notasValidas[i].replace(".json", "")

    geralSearch = consultas.geralSearch(teste3)
    consulta_c = consultas.consulta_c(teste3)
    consulta_d = consultas.consulta_d(teste3)
        
    app.run(debug=True)