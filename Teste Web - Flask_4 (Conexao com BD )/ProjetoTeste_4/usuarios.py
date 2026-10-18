import conexao

class Usuario:
    # Método GET (leitor)
    def get_nome(self):
        return self.__nome

    # Método SET (modificador)
    def set_nome(self, novo_nome):
        self.__nome = novo_nome
        print(self.__nome)


    def salvarDadoBanco(self):
        conn= conexao.conectar()
        cursor = conn.cursor()
          # conn.cursor() =>
          # Vem de dentro do pacote interno do mysql-connector-python.
          # É a biblioteca que "ensina" o objeto de conexão a ter esse método.

        sql = "INSERT INTO usuario (nome_usuario) VALUES ('" + self.__nome + "')"
        print(sql)

        cursor.execute(sql)

        conn.commit()  # confirma a gravação
        cursor.close()
        conn.close()
         # Porque devo fechar a conexão?
         # A cada requisição no seu Flask abre uma conexão e nunca fecha,
         #Limite máximo de 150 conexões depois disso apresenta um erro por excesso de conexao