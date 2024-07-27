


lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100, 200, 300, 400, 500]

number = [numero for numero in lista if numero < 10]
# print(number)


# numeros = [
#     numero if numero != 6 else 600 for numero in lista if numero < 10
# ]

# numeros = [numero if numero != 6 else 600 for numero in number]


numeros = [ (x,y) if x != 2 else 'nan' for x in range(10) for y in range(2)

]
print(numeros)


# nova_lista = []
# for numero in lista:
#  if numero > 10:
#   nova_lista.append(numero)
# print(nova_lista)


