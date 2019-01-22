
# criando e adicionando
lista = []
lista.append(1)
lista.append(2)
lista.append([2,3,4])
lista

# criando e removendo e revertendo
lista = [1, 2, "Robson", "Ana"]
lista
lista.remove(2)
lista
lista.reverse()
lista

# acessando elementos
lista = [1, 4, "Antonio", "Aparecida", 3.1415]
lista.index("Aparecida")
lista[4]
lista[-1]

# acessando elementos com range
lista = ["Ana", "Lia", "Rui", "Paulo", "Dani"]
lista[1:3]
lista[1:-1]
lista[1:]
lista[:]
lista[::2]
lista[::-1]