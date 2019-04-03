from random import randint

nunero_informado = -1
numere_secreto = randint(0,9)

while nunero_informado != numere_secreto:
    nunero_informado = int(input("Informe o número: "))

print('Número secreto {} foi encontrado'.format(numere_secreto))