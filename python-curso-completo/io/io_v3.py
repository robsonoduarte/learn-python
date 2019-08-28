arquivo = open('pessoas.csv')


for line in arquivo:
    print('Nome: {}, Idade: {}'.format(*line.strip().split(',')))
arquivo.close()