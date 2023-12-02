def calcular_patos_coelhos(total_cabecas, total_pes):
    coelhos = (total_pes - 2 * total_cabecas) / 2
    patos = total_cabecas - coelhos
    return int(patos), int(coelhos)

total_cabecas = int(input("Insira o total de cabeças: "))
total_pes = int(input("Insira o total de pés: "))

resultado_patos, resultado_coelhos = calcular_patos_coelhos(total_cabecas, total_pes)
print(f"Total de patos: {resultado_patos}")
print(f"Total de coelhos: {resultado_coelhos}")