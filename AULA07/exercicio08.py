# Faça um programa que receba um número inteiro maior
# que 1. Ele deve verificar se o número fornecido é primo
# ou não, e mostrar a mensagem correspondente.
# Lembre-se: um número primo só é divisível por 1 ou por
# ele mesmo.

k = int(input("Entre com o valor: "))
primo = True
n = 0

for i in  range(1, k+1):
    if (k % i) == 0:
        n = n+1
if n > 2:
    primo = False
if primo:
    print(f"O número {k} é primo")
else:
    print(f"O número {k} não é primo")