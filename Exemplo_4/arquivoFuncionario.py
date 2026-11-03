class Funcionario:

    def __init__(self, nome, nascimento,):
        self.__nome = nome
        self.nacimento = nascimento
        self.cep =None
        self.endereco =None

    #props
    @property
    def nomeFuncionario(self):
        return self.__nome

    @nomeFuncionario.setter
    def nomeFuncionario(self, value):
        self.__nome=value


