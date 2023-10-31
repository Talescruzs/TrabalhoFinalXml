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
        consulta_a=consulta_a, consulta_b=consulta_b, 
        consulta_c=consulta_c, qtdMenor=len(consulta_c.values()), notasMenor=list(consulta_c.keys()))

@app.route('/notas/<name>')
def notas(name):
    return render_template(
        "nota.html", notasValidas=notasValidas, 
        qtdNotas=len(notasValidas), consulta=consulta_a, 
        qtdProdutos=consulta_a["qtdProdutos"][name+".json"],
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

    consulta_a = consultas.consulta_a(teste3)
    consulta_b = consultas.consulta_b(teste3)
    consulta_c = consultas.consulta_c(teste3)
        
    app.run(debug=True)