def calculo_soma_multiplicacao(numero):
    soma = 0
    multiplicacao = 1

    for entrada in numero:
        digito = int(entrada)
        soma += digito
        multiplicacao *= digito

    return soma, multiplicacao

numero = input("Digite um número: ")

soma, multiplicacao = calculo_soma_multiplicacao(numero)
print(f"Soma = {soma} e Multiplicação = {multiplicacao}")