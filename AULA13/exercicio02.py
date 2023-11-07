# Faça uma função que retorne o valor lógico V (verdadeiro) se o número inteiro
# passado por parâmetro for primo, e F (falso) se não. Implemente sua função
# em um programa completo.

def ehprimo(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

valor = int(input("Difite o valor: "))

if ehprimo(valor):
    print("O valor é primo")
else:
    print("O valor não é primo")
