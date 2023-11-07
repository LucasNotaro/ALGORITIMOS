# Crie uma função que receba como parâmetro
# 3 números interios (representando horas,
# minutos e segundos). A função deve
# converter em segundos.
# Por exemplo: 2 h, 40 min e 10 segundos
# correspondem a 9.610 segundos

def segundos(h, m, s):
    return (h * 3600 + m * 60 + 5)

hora = int(input("Digite a hora: "))
minutos = int(input("Digite os minutos: "))
seg = int(input("Digite os segundos: "))

print(f"O total de segundos é {segundos(hora, minutos, seg)} segundos.")