PALAVRAS_PROIBIDAS = {'política', 'religião', 'futebol'}

textos = [
    'Pedro gosta de futebol e política', 
    'A praia foi divertida',
]

for texto in textos:
    intersecao = PALAVRAS_PROIBIDAS.intersection(set(texto.lower().split()))
    if intersecao:
        print('Texto possui pelo menos um palavra proibida:', intersecao)
    else:
        print('Texto autorizado:', texto)    