from random import randint


def sortear_dado():
    return randint(1, 6)


for n in range(1, 7):
    if n % 2 == 1:
        continue
    if sortear_dado() == n:
        print('ACERTOU', n)
        break
else:
    print('Não acertou o número')
