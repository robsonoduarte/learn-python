
# os tipos de numeros do pythons são:

a = 1 #int
b = 2.2 # float

print(type(a))
print(type(b))


from decimal import Decimal, getcontext

print(Decimal(1) / Decimal(7)) # usando o Decimal para aumentar a precisão

getcontext().prec = 4 # ajustando a precisão do Decimal 

print(Decimal(1) / Decimal(7)) 

print(1.1 + 2.2) # não utiliza a precisão ajustada do decimal 
print(Decimal(1.1) + Decimal(2.2))



