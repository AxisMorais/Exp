class Usuario:
    # Método GET (leitor)
    def get_nome(self):
        return self.__nome

    # Método SET (modificador)
    def set_nome(self, novo_nome):
        self.__nome = novo_nome
        print(self.__nome)
