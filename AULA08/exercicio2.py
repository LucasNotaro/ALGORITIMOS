data = input("Digite a data no formato dd/mm/aaaa: ")
dia = data[0:2]
mes = data[3:5]
ano = data[6:10]

data2 = ano+mes+dia
print(f"{ano}{mes}{dia}")
print(data2)
print(data[::-1])

