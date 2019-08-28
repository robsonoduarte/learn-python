import csv

with open('pessoas.csn') as entrada:
    for pessoas in csv.reader(entrada):
        print('Nome: {}, Idade: {}'.format(*pessoas))