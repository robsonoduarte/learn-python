
try:
    arquivo = open('pessoas.csv')

    for line in arquivo:
        print('Nome: {}, Idade: {}'.format(*line.strip().split(',')))

finally:
    arquivo.close()


if arquivo.closed:
    print("Arquivo fechado")    