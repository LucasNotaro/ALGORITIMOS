# Faça um algoritmo que receba o ano de nascimento de uma pessoa e o ano atual e mostre:
# a) A idade dessa pessoa em anos;
# b) A idade dessa pessoa em meses;
# c) A idade dessa pessoa em dias;
# d) A idade dessa pessoa em semanas.


Nascimento = int(input("digite o ano de nascimento: "))
Ano = int(input("digite o ano atual: "))


Idade_anos = Ano - Nascimento
Idade_meses = Idade_anos*12
Idade_dias = Idade_anos*365
Idade_semanas = Idade_anos*53

print(Idade_anos, "anos")
print(Idade_meses, "meses")
print(Idade_dias, "dias")
print(Idade_semanas, "semanas")
