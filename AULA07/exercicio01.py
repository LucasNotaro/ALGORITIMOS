# Faça um algoritmo que leia dois valores b e N
# inteiros e positivos, calcule e mostre o valor
# E, conforme a fórmula a seguir.
# E = (b ** 1) + (b ** 2) + (b ** 3) + ... + (b ** N)

e=0
n = int(input("Digite o valor de N: "))

for i in range (1, n+1):
    e = e + (2 ** i)
print(f"O valor de e = {e}")