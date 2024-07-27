"""
O metodo split() fatia uma string e coloca dentro de uma lista
"""

lista = 'Minha terra tem palmeiras onde canta o sabiá'

lista2 = lista.split()
# print(lista2)


'''
O strip() é usado para remover espaços dentro de uma string 
Rstrip() usado para remover espaços na direita
lstrip() usado para remover espaços na esquerda

'''

lista_palavras = '  Minha terra tem palmeiras onde canta o sabiá'.lstrip()
print(lista_palavras)



lista_palavras2 = '  Minha terra tem palmeiras onde canta o sabiá             '.rstrip()
# print(lista_palavras2)



'''
Join() une uma string
'''



frase_froma = ' Minha terra tem palmeiras onde canta o sabiá'

frase = frase_froma.join(frase_froma)

print(frase)