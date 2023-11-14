# Função para validar um CPF
def validar_cpf(cpf):
    # Remove pontos e traços do CPF
    cpf = cpf.replace(".", "").replace("-", "")

    # Verifica se o CPF tem 11 dígitos
    if len(cpf) != 11:
        return False

    # Calcula o primeiro dígito verificador
    soma = 0
    for i in range(9):
        # Multiplica cada dígito por um peso específico
        soma += int(cpf[i]) * (10 - i)

    # Calcula o resto da divisão por 11
    resto = (soma * 10) % 11

    # Se o resto for 10 ou 11, considera como 0
    if resto == 10 or resto == 11:
        resto = 0

    # Verifica se o primeiro dígito verificador está correto
    if resto != int(cpf[9]):
        return False

    # Calcula o segundo dígito verificador
    soma = 0
    for i in range(10):
        # Multiplica cada dígito por um peso específico
        soma += int(cpf[i]) * (11 - i)

    # Calcula o resto da divisão por 11
    resto = (soma * 10) % 11

    # Se o resto for 10 ou 11, considera como 0
    if resto == 10 or resto == 11:
        resto = 0

    # Verifica se o segundo dígito verificador está correto
    if resto != int(cpf[10]):
        return False

    # Se passou por todas as verificações, o CPF é válido
    return True

# Solicita ao usuário que digite o CPF
cpf = input("Digite o CPF: ")

# Chama a função de validação e imprime o resultado
if validar_cpf(cpf):
    print("CPF válido")
else:
    print("CPF inválido")

# # Função para validar um CPF
# def validar_cpf(cpf):
#     # Remove pontos e traços do CPF
#     cpf = cpf.replace(".", "").replace("-", "")
#
#     # Verifica se o CPF tem 11 dígitos
#     if len(cpf) != 11:
#         return False
#
#     # Calcula o primeiro dígito verificador
#     soma = 0
#     for i in range(9):
#         # Multiplica cada dígito por um peso específico
#         soma += int(cpf[i]) * (10 - i)
#
#     # Calcula o resto da divisão por 11
#     resto = (soma * 10) % 11
#
#     # Se o resto for 10 ou 11, considera como 0
#     if resto == 10 or resto == 11:
#         resto = 0
#
#     # Verifica se o primeiro dígito verificador está correto
#     if resto != int(cpf[9]):
#         return False
#
#     # Calcula o segundo dígito verificador
#     soma = 0
#     for i in range(10):
#         # Multiplica cada dígito por um peso específico
#         soma += int(cpf[i]) * (11 - i)
#
#     # Calcula o resto da divisão por 11
#     resto = (soma * 10) % 11
#
#     # Se o resto for 10 ou 11, considera como 0
#     if resto == 10 or resto == 11:
#         resto = 0
#
#     # Verifica se o segundo dígito verificador está correto
#     if resto != int(cpf[10]):
#         return False
#
#     # Se passou por todas as verificações, o CPF é válido
#     return True
#
# # Solicita ao usuário que digite o CPF
# cpf = input("Digite o CPF: ")
#
# # Chama a função de validação e imprime o resultado
# if validar_cpf(cpf):
#     print("CPF válido")
# else:
#     print("CPF inválido")

# cpf.replace(".", "").replace("-", ""):
#
# Esta linha utiliza o método replace() para remover pontos (.) e traços (-) da string cpf. O método replace() substitui as ocorrências de uma substring por outra.
# len(cpf):
#
# A função len() retorna o comprimento da string cpf, ou seja, o número de caracteres presentes na string. Neste contexto, está sendo usado para verificar se o CPF tem exatamente 11 dígitos.
# for i in range(9): e for i in range(10)::
#
# Estas são estruturas de repetição for que iteram sobre uma sequência de valores. No primeiro caso, itera de 0 a 8, e no segundo caso, itera de 0 a 9. Ambos os loops são usados para calcular a soma ponderada dos dígitos do CPF.
# int(cpf[i]):
#
# A função int() converte uma string para um número inteiro. Aqui, é usada para converter cada dígito do CPF de string para inteiro, permitindo operações aritméticas.
# (10 - i) e (11 - i):
#
# Essas expressões representam os pesos aplicados aos dígitos do CPF durante o cálculo. À medida que o loop avança, os pesos variam de 10 a 1.
# (soma * 10) % 11:
#
# Calcula o resto da divisão por 11 da soma multiplicada por 10. Este é um passo crucial na verificação dos dígitos verificadores do CPF.
# if resto == 10 or resto == 11: e resto = 0:
#
# Se o resto for 10 ou 11, é considerado como 0. Isso é feito porque o CPF utiliza dígitos verificadores que podem ser 10 ou 11, mas no cálculo, eles são representados como 0.
# if resto != int(cpf[9]): e if resto != int(cpf[10])::
#
# Verifica se o dígito verificador calculado (resto) é igual ao nono e décimo dígitos do CPF. Se não forem iguais, o CPF é considerado inválido.
# return True:
#
# Se todas as verificações passarem, a função retorna True, indicando que o CPF é válido.
# cpf = input("Digite o CPF: "):
#
# Solicita ao usuário que digite o CPF.
# if validar_cpf(cpf)::
#
# Chama a função validar_cpf com o CPF inserido pelo usuário e verifica se o retorno é True.
# print("CPF válido") e print("CPF inválido"):
#
# Imprime se o CPF é válido ou inválido com base no retorno da função.