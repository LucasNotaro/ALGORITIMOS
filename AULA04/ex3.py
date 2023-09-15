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
