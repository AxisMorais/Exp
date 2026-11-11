import ArquivoAdvogado
import ArquivoFinanceiro
import ArquivoUsuario

if __name__ == '__main__':

    meuObjetoCadastradorAdvogado = ArquivoAdvogado.Advogado()
    resultado = meuObjetoCadastradorAdvogado.cadastrarUsuario("João", "OAB200" )

    print(resultado)

    meuObjetoCadastradorAdm = ArquivoFinanceiro.Financeiro()
    resultadoII = meuObjetoCadastradorAdm.cadastrarUsuario("Ana","CPA0120B")

    print(resultadoII)


