from flask import Flask, render_template
from Files import Validator, Files
from Search import Search
import consultas

app = Flask(__name__)

files = Files("notasFiscais/", "Json/")
validate = Validator(files, "schema.json")
search = Search(validate)

notasValidas = list(search.validFiles.keys())
for i in range(len(notasValidas)):
    notasValidas[i] = notasValidas[i].replace(".json", "")

geralSearch = consultas.geralSearch(search)
consulta_c = consultas.consulta_c(search)
consulta_d = consultas.consulta_d(search)

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
        name=name,
        detalhesNota=consultas.detalhesNota(search, name+".json")
        )

if __name__ == "__main__":
    files = Files("notasFiscais/", "Json/")
    validate = Validator(files, "schema.json")
    search = Search(validate)
    
    notasValidas = list(search.validFiles.keys())
    for i in range(len(notasValidas)):
        notasValidas[i] = notasValidas[i].replace(".json", "")

    geralSearch = consultas.geralSearch(search)
    consulta_c = consultas.consulta_c(search)
    consulta_d = consultas.consulta_d(search)
    
        
    app.run(debug=True)