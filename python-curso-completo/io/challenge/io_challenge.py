import csv

with open('ibge.csv', encoding='ISO-8859-1') as file:
    reader = csv.DictReader(file)
    next(reader, None)
    for line in reader:
        #print(line['nome_orige'] + line['nome_desti'])
        print(f'Nome: {line["nome_orige"]}, Idade: {line["nome_desti"]}')