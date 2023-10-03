palavra = input("digite a palavra: ")

frente = palavra
tras = palavra[::-1]

if frente.lower() == tras.lower():
    print(f"A palavra {palavra} é palindroma")
else:
    print(f"A palavra {palavra} não é palindroma")