arquivo = open('pessoas.csv')


for line in arquivo:
    print('Nome: {}, Idade: {}'.format(*line.split(',')))
arquivo.close()