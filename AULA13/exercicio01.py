# Faça uma função que retorne o valor lógico V (verdadeiro) se o número inteiro passado por
# parâmetro for par, e F (falso) se não. Implemente sua função em um programa completo.

def ehpar(numero):
    if x % 2 == 0:
        return True
    else:
        return False

x = int(input("digite o valor: "))

if ehpar(x):
    print(f"O número {x} é par.")
else:
    print(f"O número {x} é impar.")