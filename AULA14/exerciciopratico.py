def valida_cpf(cpf):
    # Remove caracteres não numéricos do CPF
    cpf = ''.join(filter(str.isdigit, cpf))

    # Verifica se o CPF tem 11 dígitos
    if len(cpf) != 11:
        return False

    # Calcula o primeiro dígito verificador
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    resto = soma % 11
    digito1 = 11 - resto if resto > 1 else 0

    # Verifica se o primeiro dígito verificador está correto
    if digito1 != int(cpf[9]):
        return False

    # Calcula o segundo dígito verificador
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    resto = soma % 11
    digito2 = 11 - resto if resto > 1 else 0

    # Verifica se o segundo dígito verificador está correto
    if digito2 != int(cpf[10]):
        return False

    # Se passou por todas as verificações, o CPF é válido
    return True

# Exemplo de uso
cpf = input("Digite o CPF (com pontos e traço): ")
if valida_cpf(cpf):
    print("CPF válido")
else:
    print("CPF inválido")
