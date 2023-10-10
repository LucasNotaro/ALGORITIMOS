lista = []
for i in range (10):
    lista.append(int(input(f"Digíte o número {i+1}: ")))

for i in lista[::-1]:
    print(i, end=" ")
print()
print(lista)