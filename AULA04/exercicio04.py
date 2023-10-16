# Faça um algoritmo que receba a data de nascimento de uma pessoa e a data atual  e mostre sua idade em
# anos, meses, semanas e dias.

# corrigir semanas <<<<>>>>>>

from datetime import datetime

# Função para calcular a idade
def calcular_idade(data_nascimento, data_atual):
    diferenca = data_atual - data_nascimento
    anos = diferenca.days // 365
    meses = (diferenca.days % 365) // 30
    dias = (diferenca.days % 365) % 30
    semanas = diferenca.days // 7
    return anos, meses, semanas, dias

# Função para validar o formato da data
def validar_data(data_str):
    try:
        data = datetime.strptime(data_str, "%d/%m/%Y")
        return True, data
    except ValueError:
        return False, None

# Solicita a data de nascimento
while True:
    data_nascimento_str = input("Digite a data de nascimento (DD/MM/AAAA): ")
    data_valida, data_nascimento = validar_data(data_nascimento_str)
    if data_valida:
        break
    else:
        print("Formato de data inválido. Digite novamente no formato DD/MM/AAAA.")

# Obtém a data atual
data_atual = datetime.now()

# Calcula a idade
idade_anos, idade_meses, idade_semanas, idade_dias = calcular_idade(data_nascimento, data_atual)

# Exibe a idade
print(f"Idade: {idade_anos} anos, {idade_meses} meses, {idade_semanas} semanas e {idade_dias} dias.")

