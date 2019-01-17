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

 




