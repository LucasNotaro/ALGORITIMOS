# Faça um algoritmo que calcule a área de um triângulo.
# Este algoritmo não pode permitir a entrada de dados
# inválidos, ou seja, medidas menores ou iguais a zero.

while True:
    base = float(input("Entre com a base:"))
    if base > 0:
        break
    print("O valor digitado é inválido")

while True:

    altura = float(input("Entre com a base:"))
    if altura > 0:
        break
    print("O valor digitado é inválido")

area = (base + altura) / 2
print(f"A área do triangulo é {area:5.2f}")