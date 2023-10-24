# Faça um algoritmo para determinar se um
# determinado vetor, digitado pelo usuário, é
# um palíndromo.
# Palíndromo: lido da direita para a esquerda,
# ou vice versa, representam a mesma coisa.
# Ex: AMA

palavra = input("digite a palavra: ")

frente = palavra
tras = palavra[::-1]

if frente.lower() == tras.lower():
    print(f"A palavra {palavra} é palindroma")
else:
    print(f"A palavra {palavra} não é palindroma")