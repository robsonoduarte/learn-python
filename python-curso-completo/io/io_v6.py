
with open('pessoas.csv') as arquivo:
    with open('pessoas.txt', 'w') as saida:        
        for line in arquivo:
            pessoa = line.strip().split(',')
            print('Nome: {}, Idade: {}'.format(*pessoa),file=saida)


if arquivo.closed:
    print("Arquivo fechado")

if saida.closed:
    print("Saida fechada")


