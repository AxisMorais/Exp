#Herança - Linguagem Orientada a Objetos
import agenteMarkting
import arquivoFuncionario

#iniciando o main
if __name__== "__main__":
    print("")

    meuObjetoFuncionario = arquivoFuncionario.Funcionario("Thiago", 2019)
    print(meuObjetoFuncionario.nomeFuncionario)


    meuObjetoAgenteMarkting = agenteMarkting.AgenteMarkting(" Markting Thiago", 1989)
    print(meuObjetoAgenteMarkting.nomeFuncionario)














