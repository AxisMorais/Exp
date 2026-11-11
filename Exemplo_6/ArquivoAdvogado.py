from ArquivoUsuario import Usuario


class Advogado(Usuario):

   def cadastrarUsuario(self, nome, documento):
       self.nome=nome
       self.OAB_documento=documento
       return "Advogado " +self.nome +" Cadastrado com sucesso"


   def cadastrarFuncao(self, funcao, numeroProcesso):
        self.funcao = funcao
        self.numeroProcesso = numeroProcesso








