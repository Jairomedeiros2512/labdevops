from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "MBA - Impacta Full Stack Developer - Aula DevSecOps - Aluno Jairo Medeiros Silva"

if __name__ == '__main__':
    app.run(debug=True)