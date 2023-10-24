# Faça um algoritmo para ler nove caracteres
# numéricos em uma string. Mostre o conteúdo
# dessa string colando pontos e virgula,
# respectivamente nas posições inteiras e
# decimais.
# Exemplo:
# Digitado> 987654321
# Mostrado> 9.876.543,21

while True:
    valor = input("Digite o valor de nove caracteres: ")
    if valor.isnumeric() and len(valor) == 9:
        break
    if valor.isnumeric():
        print("Necessário ser 9 dígitos")
    else:
        print("Digite apenas números")

novo_valor = valor[0] + "." + valor[1:4] + "." + valor [4:7] + "," + valor[7] + valor [8]
print(novo_valor)