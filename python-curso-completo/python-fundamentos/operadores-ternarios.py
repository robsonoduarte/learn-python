a = ('False', "True")[True]
print(a)


a = ('False', "True")[False]
print(a)


a = ('True' if True else "False")
print(a)


a = ('True' if False else "False")
print(a)