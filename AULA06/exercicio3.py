# Faça um algoritmo que calcula a qtd de latas de tinta necessária para pintar um aposento. O algoritmo deve receber
# como entradas as dimensões desse aposento (largura e comprimento) e a quantidade, em litros, da lata de tinta. Considere
# ainda: O pé-direito do aposento mede 2,80m; deverão ser pintadas apenas as paredes. O aposento tem apenas uma porta,
# medindo 0,80m x 2,10m. Cada litro de tinta pinta, aproximadamente, 3 metros quadrados.

largura = float(input("Informe a largura do aposento (metros): "))
comprimento = float(input("Informe o comprimento do aposento (metros) : "))
altura_parede = 2.80

lata = 18.00
galao = 3.60
litro = 1.00

area_total_paredes = 2 * (largura + comprimento) * altura_parede

area_porta = 0.80 * 2.10

area_paredes_pintar = area_total_paredes - area_porta

litros_por_lata = float(input("Digite quantos litros terá a lata de tinta usada (disponível apenas 1, 3.6 ou 18): "))


litros_necessarios = area_paredes_pintar / 3

quantidade_latas = litros_necessarios / litros_por_lata

quantidade_latas = int(quantidade_latas)
if litros_necessarios % litros_por_lata != 0:
    quantidade_latas += 1

print(f"É necessário {quantidade_latas} latas de tinta para pintar o aposento.")