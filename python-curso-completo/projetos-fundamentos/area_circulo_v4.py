from math import pi


def circulo(raio):
    return pi * float(raio) ** 2


if __name__ == '__main__':
    area = circulo(input("Informe o raio: "))
    print('Área do círculo => ', area)
