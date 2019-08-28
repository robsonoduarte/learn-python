
with open('pessoas.csv') as arquivo:
    for line in arquivo:
        print('Nome: {}, Idade: {}'.format(*line.strip().split(',')))


if arquivo.closed:
    print("Arquivo fechado")


