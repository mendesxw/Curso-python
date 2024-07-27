

import os

palavraSecreta = 'nabucodonozar'
letrasPalavra = ''
tentativas = 0

while True:

   tentativas +=1
   
   palavraDigitada = input('Digite uma letra: ')

   if len(palavraDigitada) > 1:
      print('Digite apenas uma letra.')
      continue
   
   if palavraDigitada in palavraSecreta:
      letrasPalavra += palavraDigitada

   palavraForma = ''

   for palavra in palavraSecreta:
      if palavra in letrasPalavra:
       palavraForma += palavra


      else:
         palavraForma += ('*')

   if palavraForma == palavraSecreta:
      os.system('cls')
      print('VOCÊ GANHOU!!')
      print(f'A palavras secretaera "{palavraSecreta}"')
      print(f'Você teve {tentativas} tentativas')
      letrasPalavra = ''
      tentativas = 0
     
   print(palavraForma)
  


# Segue no insta @mendesxw0d
