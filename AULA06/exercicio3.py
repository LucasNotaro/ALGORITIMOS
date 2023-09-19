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