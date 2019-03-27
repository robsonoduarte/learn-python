from math import pi
import sys
import errno


class TerminalColor:
    ERR0 = '\033[91m'
    NORMAL = '\033[0m'


def help():
    print('Informe a raio do circulo')


def circulo(raio):
    return pi * float(raio) ** 2


if __name__ == '__main__':
    if(len(sys.argv)) < 2:
        help()
    elif not sys.argv[1].isnumeric():
        print(TerminalColor.ERR0 +
              "O raio deve ser um valor numerico" + TerminalColor.NORMAL)
    else:
        area = circulo(sys.argv[1])
        print('Area do circulo => ', area)
