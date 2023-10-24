# Faça um algoritmo que leia uma matriz 2x2 e
# imprima os seus elementos na ordem:
# 1,1 =
# 1,2 =
# 2,1 =
# 2,2 =
# Obs: linha, coluna

lista = []
for i in range (10):
    lista.append(int(input(f"Digíte o número {i+1}: ")))

lista.reverse()
print(lista)
