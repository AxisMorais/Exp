
#`Passo 1 Instalar o flask  pip install falsk
# Passo 2 Ativá-lo no Pycharm 4 Barrinhas >> Settings>>Project>>PythonInterpreter
# Passo 3 Importar o Flask  (linha abaixo)
from flask import Flask, render_template

#iniciar o flask  criando a variável app
app = Flask(__name__)

#Criar uma rota
@app.route("")
def paginaInicio():
    return render_template("index.html")

#chamar o metodo principal
if __name__ == "__main__":
    app.run(debug = True)