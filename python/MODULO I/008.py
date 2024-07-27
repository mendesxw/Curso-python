

'''
Estou pegando os itens da lista, e inumerando de acordo com seus indices. 
para isso, utilizo o metodo enumerate(), que recebe como argumento a segunda lista
'''

lista = ['lucas', 'gabriel', 'mendes', 'leite']
lista2 = enumerate(lista)
print(lista2)

for item in lista2:
    print(item)


# outras formas de fazer isso


'''
Este valor só conseguimos utilizar uma unica vez. Caso aja necessidade de utilizar novamente, ficamos refem desse 'erro'.
para evitar este erro, utilizamos a propriedade enumerate() diretamente na condicional utilizada
'''

lista_3 = ['lucas', 'gabriel', 'mendes', 'leite']

for item in enumerate(lista_3):
    print(f'agora sim podemos utilizadar o {item} outras vezes')

'''
Para que possamos utilizar este mesmo valor só que fora de uma condicional fazemos uma conersão de type para list()
ou tuple().
'''


lista04 = ['lucas', 'gabriel', 'mendes', 'leite']

lista_convertida = list(enumerate(lista04))
print(lista_convertida)

'''
O Python, me retornará o seguinte código:
[(0, 'lucas'), (1, 'gabriel'), (2, 'mendes'), (3, 'leite')]
'''