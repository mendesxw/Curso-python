"""
Neste exercico, criarei um gerador de CPF, que verifca os dois ultimos digitos para fazer a verificação de um CPF

CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7



#################################################


Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0



"""

coletarCpf = input('Digite o CPF para verifcação: ')
 
try:
    coletarCpf = int(coletarCpf)    

except ValueError:
    print('CPF invalido. Digite apenas números ou verifique se não contém espaços.')

numero = 10
resultado = 0
for verificar in str(coletarCpf):
      trasferencia = int(verificar)
      conta = (trasferencia * numero) 
      resultado += (conta * 10)
      divide = resultado % 11
      numero -= 1

divide = str(divide)
if divide:
     divide = int(divide)
     if divide <=9:
          print(divide)
     else:
        print( 0)

digitodez = coletarCpf + divide
numero2 = 11
resultado2 = 0

for digito in str(digitodez):
     resultado2 += int(digito) * numero2
     numero2 -= 1
     multiRes = (resultado2 * 10) % 11
     
multiRes = str(multiRes)

if multiRes:
     multiRes = int(multiRes)
     if multiRes <= 9:
          print(multiRes)
    
     else:
          print(0) 
     

print(divide , multiRes) 




