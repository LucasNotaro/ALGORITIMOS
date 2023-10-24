# Elabore um algoritmo para determinar
# quantas vogais existem dentro de uma
# determinada frase (que deve ser recebida do
# usuário)

frase = input("digite uma frase: ")
qtd = 0
for letra in frase:
    if letra.lower() in "aeiou":
        qtd = qtd +1

print(f"A frase possui {qtd} vogais")