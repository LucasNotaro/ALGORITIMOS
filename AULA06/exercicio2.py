# Desenvolva um algoritmo para calcular e mostrar o desconto no valor de uma compra (fornecido pelo usuário), de
# acordo com a tabela:
# Valor Desconto
# Até R$ 1000,00 10%
# De R$ 1001,00 a R$ 5000,00 20%
# Acima de R$ 5000,00 30%

valor_compra = float(input("Digite o valor da compra: R$ "))

if valor_compra <= 1000.00:
    desconto = valor_compra * 0.10

elif valor_compra <= 5000.00:
    desconto = valor_compra * 0.20

else:
    desconto = valor_compra * 0.30
valor_final = valor_compra - desconto

print(f"Desconto: R$ {desconto:8.2f}")