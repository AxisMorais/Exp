from urllib import request

#Importando a classe usuário

#`Passo 1 Instalar o flask  pip install falsk
# Passo 2 Ativá-lo no Pycharm 4 Barrinhas >> Settings>>Project>>PythonInterpreter
# Passo 3 Importar o Flask  (linha abaixo)
from flask import Flask, render_template, request

import usuarios
from usuarios import Usuario

#iniciar o flask  criando a variável app
app = Flask(__name__)

#------------------
#ROTAS
#---------------------
#Criando as  Rotas
@app.route("/")
def paginaInicio():
    return render_template("index.html")


@app.route('/enviar', methods=['POST'])
def receber_dados():
    # 1. Captura o dado que veio do formulário HTML
    nome_recebido = request.form.get('nome_usuario')

    #2 Criar um objeto da classe usuário
    objUsuario = usuarios.Usuario()

    #3 Enviado  o dado para o arquivo usuário pelo metodo set
    objUsuario.set_nome(nome_recebido)

    #4. Usa o método GET para pegar o nome de dentro do objeto
    nomeEncapsulado = objUsuario.get_nome()

    #5. Devolve para a tela o nome insformado pelo usuário
    return 'Nome informado: <br>' + nomeEncapsulado

#chamar o metodo principal
if __name__ == "__main__":
    app.run(debug = True)