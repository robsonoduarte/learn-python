dir(str)
nome = 'Robson Duarte'
nome[0]
# nome[0] = 'P' String são imutaveis

"Marca d' água" == 'Marca d\' água' #podemos "escapar" a string ou utilizar "

texto = 'Texto entre apostrófos pode ter "apasa"'

doc = """Texto com múltiplas 
...linhas"""
print(doc)

print('Texto com múltipla...\n linhas')

doc = '''Também é possível... 
com 3 aspas simples'''
print(doc)


#acessando os elementos da string

nome[0] #direita para esquerda
nome[7]
nome[-3] #esquerda para direita
nome[4:] #range da direita para esquerda apartir do indice 4
nome[-5:] #range  esquerda.. apartir do indice -5
nome[:3] # range da dire.. apartir do inicio da string até o indice -1
nome[2:5] # range

numeros = "1234567890"
numeros[::]
numeros[::2] #step de dois em dois
numeros[1::2] # step apartir do indice 1
numeros[::-1] # step do final para o inicio

frase = "Python é uma linguagem excelente"
'py' in frase
'ing' in frase
len(frase)
frase.lower()
frase.upper()

frase.split()
frase.split('a')

help(str.center) # help para funcões 

# python magic methods https://www.python-course.eu/python3_magic_methods.php

a = "123"
b = " Duarte "
a + b
a.__add__(b)
str.__add__(a,b)
len(a)
a.__len__()
'1' in a
a.__contains__('1')