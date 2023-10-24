# Faça um algoritmo que carregue uma tupla de 10 elementos numéricos inteiros.
# Após a finalização da entrada, o algoritmo deve escrever a mesma tupla, na ordem
# inversa de entrada.

# # Inicializa a variável 'i' com 0. Esta variável será usada como contador.
# i = 0
#
# # Inicializa uma lista vazia chamada 'lista'. Esta lista armazenará os números digitados pelo usuário.
# lista = []
#
# # Este é um loop while que continuará até que 'i' seja menor que 10.
# while i < 10:
#     # Solicita ao usuário para digitar um número. O número digitado é convertido
#     para um inteiro e armazenado na variável 'x'.
#     x = int(input("Digíte um número: "))
#     
#     # O número digitado pelo usuário é adicionado ao final da lista.
#     lista.append(x)
#
#     # Incrementa o contador 'i' em 1.
#     i = i + 1
#
# # Converte a lista de números em uma tupla e armazena na variável 't'.
# t = tuple(lista)
#
# # Imprime a tupla 't'.
# print(t)
#
# # Imprime a tupla 't' em ordem inversa.
# print(t[::-1])

lista = []
i = 0
while i < 10:
    x = int(input("Digíte um número: "))
    lista.append(x)
    i = i + 1
t = tuple(lista)

print(t)
print(t[::-1])
