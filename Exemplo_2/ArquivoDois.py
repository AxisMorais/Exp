import ArquivoUm

class ClasseB:

    def ExibirFrase(self):
        print("Essa é a mensagem da Classe B")


    meuObjetoPegador = ArquivoUm.ClasseA()
    #Valor_A está privado não é acessado pelas demais classes.
    meuObjetoPegador.mostrarValorDeA()
    #print(meuObjetoPegador.valorA)
    print(meuObjetoPegador.mostrarValorDeA())
