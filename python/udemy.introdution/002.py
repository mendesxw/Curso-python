

"""
neste arquivo, estará armazenado tudo que eu estarei estudando sobre list
(listas ou arrays), exceto os exercícios que colocarei na pasta de exercícios.

Na última aula, tive contato com minha primeira lista e alguns métodos do Python
para fazer a mudanças em lists mutáveis.

Os métodos foram: 

pop()
 que remove o ultimo elemento de uma lista. Também posso remover qualquer valor 
passando o seu indice como parâmetro e consigo retornar esse elemento em forma de variável.

  ---------------------------------

del
 remove o item que precisar, acessando pelo indice.

ex: ==> lista = [10 , 20 , 30 , 40]
 del lista[1]

  ---------------------------------

append()
 adiciona um item ao fim da sua lista. 

  ---------------------------------

insert()
adiciona um item em qualquer posição da lista caso tenha passagem de parametro
caso não tenha, adiciona ao fim da lista.

"""

lista02 = ['Lucas' , 20 , 30 , 'Gabriel']

lista02[3] = 'mendes'
secun =  lista02.pop(0)
print(lista02)
print(f'O item removido foi "{secun}"')

"""
---------------------------------
"""

lista = [10 , 20 , 30 , 40]
del lista[1]

# print(lista)


"""
----------------------------------
"""
#             0         1        2         
lista03 = ['Quarto', 'Sala', 'Banheiro']
#              -1      -2        -3          

lista03.append('Cozinha' )
# print(lista03)

"""
----------------------------------
"""

lista04 =  [
    'Lucas', 2, 3 , 4 , 5, '6'
 ]

lista04.insert(0 , 'Gabriel')
# print(lista04)


"""
Para concatenar uma lista em outra lista, podemos fazer de duas formas.
A primeira é de com o sinal de + 
e a segunda é utilizando o método extend()
"""

lista_a = [1, 2 , 3 , 4]
lista_b = [5, 6 , 7 , 8]

lista_c = lista_a + lista_b

# print(lista_c)

'''
Segunda forma
'''

lista_a = [1, 2 , 3 , 4]
lista_b = [5, 6 , 7 , 8]

lista_a.extend(lista_b)

# print(lista_a)


"""
A segunda forma, ela não retona o valor diretamente na lista_c, mas sim na lista_a.

Isso acontece pq este método é usado como extend (extender).
"""