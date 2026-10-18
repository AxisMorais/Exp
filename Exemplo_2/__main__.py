import ArquivoUm
import ArquivoDois


if __name__ == "__main__":

    meuObjetoUm =  ArquivoUm.ClasseA()
    meuObjetoDois = ArquivoDois.ClasseB()


    meuObjetoUm.mostrarMensagem()
    meuObjetoDois.ExibirFrase()

    #print("Valor vindo de A é: " , meuObjetoUm.valorA)
    print("O valor de A Acessado pelo método é:", meuObjetoUm.mostrarValorDeA())




