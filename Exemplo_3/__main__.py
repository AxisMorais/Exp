
import arquivoUm
import arquivoDois
from arquivoDois import PessoaDois

if __name__ == "__main__":

    meuObjetoTesteUm = arquivoUm.PessoaUm()

   #Sem construtor atribui um por um
    meuObjetoTesteUm.nome="Julia"
    meuObjetoTesteUm.idade=10
    print("Nome: " , meuObjetoTesteUm.nome )
    print("Idade: ", meuObjetoTesteUm.idade)

   #--------------------------------------

   #Com construtor atribui tudo de uma vez só
    meuObjetoTesteDois = arquivoDois.PessoaDois("João",17)
    print("Nomme: ", meuObjetoTesteDois.nome, "  idade:" , meuObjetoTesteDois.idade )



