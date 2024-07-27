
"""
Quando eu quiser pegar um unico valor dentro de uma lista, utilizo o desempacotamento.
 Que funciona da seguite forma

"""

nomes = ['Lucas' , 'Gabriel' , 'Mendes' , 'Leite']

nome1, nome2, nome3, nome4 = nomes

print(nome1)


# ou

a, b, c, d, e  = ['a' , 'b', 'c', 'd', 'e']
print(a)
_, b, *_  = ['add' , 'bbbb', 'c', 'd', 'e']
print(b)