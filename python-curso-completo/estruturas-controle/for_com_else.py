PALAVRAS_PROIBIDAS = ('política', 'religião', 'futebol')

textos = [
    'Pedro gosta de futebol e política',
    "A praia foi divertida",
]

for texto in textos:
    for palavra in texto.lower().split():
        if palavra in PALAVRAS_PROIBIDAS:
            print("Texto possui pelo menos um palavra proibida:", palavra)
            break
    else:
        print("Texto autorizado:", texto)
