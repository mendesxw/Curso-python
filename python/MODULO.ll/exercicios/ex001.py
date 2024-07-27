"""
Este programa pede que o usuario digite numeros
para que ele faça a soma de todos os numeros digitados
"""


pegarNum = input('Digite números para ser somado ')

try:
    pegarNumFloat = float(pegarNum)
except:
    error = 'Apenas números aceitos.'
    print(error)
def somarNumeros(*args):

    somar = 0
    for numeroSomar in args:
          pegarNumFloat = numeroSomar
          somar += numeroSomar
          return somar
    
resultSomar = somarNumeros(*pegarNum)
print(resultSomar)