"""
152.

Nesta aula, vi mais um pouco sobre tratagem de erros com raise.

Consigo tratar erros e criar meu proprio erro tambem.

EX:
"""
def resultErrorFunctionCalculadora( m):
   if m == 0:
      raise ZeroDivisionError('Sua divisão não pode ser executada.')

def divisionStringError(n):
   if not isinstance(n, (float, int)):
      raise TypeError(f'{n} deve ser int ou float' )
   
def calculadora(n,m):

    resultErrorFunctionCalculadora(m)
    divisionStringError(m)
    divisionStringError(n)
    return n / m

print(calculadora(0,0))

# def nao_aceito_zero(d):
#     if d == 0:
#         raise ZeroDivisionError('Você está tentando dividir por zero')
#     return True


# def deve_ser_int_ou_float(n):
#     tipo_n = type(n)
#     if not isinstance(n, (float, int)):
#         raise TypeError(
#             f'"{n}" deve ser int ou float. '
#             f'"{tipo_n.__name__}" enviado.'
#         )
#     return True


# def divide(n, d):
#     deve_ser_int_ou_float(n)
#     deve_ser_int_ou_float(d)
#     nao_aceito_zero(d)
#     return n / d


# print(divide(8, '0'))