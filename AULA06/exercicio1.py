# Exercício 1: Faça um algoritmo para ler um número e mostrar se ele é par ou impar, positivo ou negativo.

numero = int(input("digíte um número inteiro: "))
if numero % 5 == 0 and numero % 3 == 0:
    print(f"{numero} é divisível por 5 e por 3.")
else:
    print(f"{numero} não é divisível por 5 e por 3.")


