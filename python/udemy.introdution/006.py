

comandoStr = input("Digite um número para dobrar: ")



try:  
    print('STR: ' , comandoStr)
    dobarNumber = float(comandoStr)
    print('NUMBER: ' , dobarNumber)
    print(f'Você digitou o número {comandoStr}, cujo seu dobro é {dobarNumber * 2}')
except:
      print("Isso Não é um número ")


# if comandoStr.isdigit():

#     print(f'Você digitou o número {comandoStr}, cujo seu dobro é {dobarNumber * 2}')

# else:
#     print("Isso Não é um número: ")