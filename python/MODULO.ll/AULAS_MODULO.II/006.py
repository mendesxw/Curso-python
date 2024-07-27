"""
150. 

Nesta aula, vi sobre tratamento de exceções com py 

EX: 
"""

one = 10
two  = 0 

try:
   result = one / two
except ZeroDivisionError as error:
    print('ZeroDivisionError')
    print(error.__class__.__name__)
