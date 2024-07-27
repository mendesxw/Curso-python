
while True:
    numero1 = input('Digite um número: ')
    numero2 = input('Digite outro número : ')

    operador = input('Digite um operador: ')

    try:
     primeiroNum = float(numero1)
     segundoNum = float(numero2)
    except:
        error = 'Não é um número'
        print(error)
        continue

    operadoresPermitidos = '+-/*'

    if operador not in operadoresPermitidos:
       print('Operador não encontrado')
       continue
    
    if len(operador) > 1:
       print('Digite apenas um operador')
       continue

    if operador == '+':
       
       print(f'O resultado da adição de {primeiroNum} + {segundoNum} é igual á: {primeiroNum + segundoNum}')

    elif operador == '-':
       print(f'O resultado da subtração de {primeiroNum} e {segundoNum} é igual á: {primeiroNum - segundoNum}')

    elif operador == '*':
       print(f'O resultado da multiplicação entre {primeiroNum} e {segundoNum} é igual á: {primeiroNum * segundoNum}')

    elif operador == '/':
      try:
          print(f'O resultado dá divisão entre {primeiroNum} e {segundoNum} é igual á: {primeiroNum / segundoNum}')
      except:
         print('Não existe divisão por 0.')

    sair = input('Quer sair?').lower().startswith('s')

    if sair is True:
       break

print('Você saiu.')
