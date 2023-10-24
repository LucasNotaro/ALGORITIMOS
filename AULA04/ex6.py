# Faça um algoritmo que receba o salário de
# um funcionário e o percentual de aumento,
# calcule e mostre o valor do aumento e o
# novo salário.

salario = float(input("Digite seu salário: "))
aumento = float(input("Digite a porcentagem de aumento: "))
salariocomaumento = (salario + (salario*(aumento/100)))

print(salariocomaumento)
print(f"Novo salário: {salariocomaumento:8.2f}")
