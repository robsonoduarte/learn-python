from math import pi
import sys


def circulo(raio):
    return pi * float(raio) ** 2


if __name__ == '__main__':
    if(len(sys.argv)) >= 2:
        area = circulo(sys.argv[1])
        print('Área do círculo => ', area)
