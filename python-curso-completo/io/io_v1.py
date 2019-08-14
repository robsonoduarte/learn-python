arquivo = open('pessoas.csv')
dados = arquivo.read()
arquivo.close()

for line in dados.splitlines():
    print('Nome: {}, Idade: {}'.format(*line.split(',')))