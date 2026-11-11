from ArquivoUsuario import Usuario


class Financeiro(Usuario):

    def cadastrarUsuario(self, nome, documento):
        self.nome =nome
        self.cpaDocumento = documento
        return "Administrador " + self.nome + " Cadastrado com sucesso"



    def cadastrarFuncao(self, funcao ):
        self.funcao = funcao
        retunr: "Função: " + self.funcao + " cadastrado com sucesso!"





