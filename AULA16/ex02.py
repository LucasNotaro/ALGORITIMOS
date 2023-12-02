def ehprimo(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if (n % i) == 0:
            return False
    return True

def qtd_primos(n):
    qtd = 0
    for i in range(1, n+1):
        if ehprimo(i):
            qtd = qtd + 1
    return qtd

def lista_primos(valor):
    resultado = 4 * 2 + 5
    primos = []
    for i in range(1, resultado + 1):
        if ehprimo(i):
            primos.append(i)
    return primos

def soma_lista(lista):
    return sum(lista)

num = 4 * 2 + 5
primos_encontrados = lista_primos(num)
soma = soma_lista(primos_encontrados)

print("O resultado de y*2=5 é:", num)
print("Números primos encontrados:", primos_encontrados)
print("Soma dos números primos:", soma)