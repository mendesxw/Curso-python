"""
151.

Nesta aula, vi sobre try, except, finally e else.

O Try, é usado para tratar expressoes e sempre vem acompanado de um except ou de finally.

O except, é utilizado para tratar expressoes e é acompanhado de um try. 

O finally, sempre executará um bloco de código. Independente do que vier por cima dele. 

O else, é usado caso não aja erro no código.

Todos eles, podem ser utilizados juntos.

EX:
"""
one = 10
two  = 0 

try: 
   result = one * two

except ZeroDivisionError:
   print('fudeu!')

else:
   print('fudeu nada')

