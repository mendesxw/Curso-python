"""
Ainda estudando set(). 
Hoje trago o metodo isinstance(), para a verificação de um tipo


"""
import math
lista = [
    1.2, 2.3, 3.4, (2,3,4), {5,6,7,8}, {'name':'Lucas'}, 
            [
                4,
                5,
                6,
                10
            ]
]

for item_list in lista:
    if isinstance(item_list, list):
        # print(item_list[:4])
         ...


for item in lista:
     if isinstance(item, float):
          expoente = item ** 2 , item
          math.ceil(expoente)
          print(item ** 2 , item, expoente)
