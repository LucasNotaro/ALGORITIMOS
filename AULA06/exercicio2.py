valor_compra = float(input("Digite o valor da compra: R$ "))

if valor_compra <= 1000.00:
    desconto = valor_compra * 0.10

elif valor_compra <= 5000.00:
    desconto = valor_compra * 0.20

else:
    desconto = valor_compra * 0.30
valor_final = valor_compra - desconto

print(f"Desconto: R$ {desconto:8.2f}")