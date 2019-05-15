PALAVRAS_PROIBIDAS = ('política', 'religião', 'futebol')

textos = [
    'Pedro gosta de futebol e política', 
    "A praia foi divertida",
]

for texto in textos:
    found = False
    for palavra in texto.lower().split():
        if palavra in PALAVRAS_PROIBIDAS:
            print("Texto possui pelo menos um palavra proibida:", palavra)
            found = True
            break

    if not found:
        print("Texto autorizado:", texto)
