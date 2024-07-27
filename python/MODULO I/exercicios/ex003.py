
entrada = input('Digite um número: ')

if entrada.isdigit():
    entrada_int = int(entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = 'ímpar'

    if par_impar:
        par_impar_texto = 'par'

    print(f'O número {entrada_int} é {par_impar_texto}')
else:
    print('Você não digitou um número inteiro')


entradaHora = input('Digite a hora atual do seu dispositivo: ')

try:
    hora = int(entradaHora)
    if hora >= 0 and hora <= 11:
        print('Bom Dia!')

    elif hora >= 12 and hora <= 17:
        print('Boa tarde!')

    elif hora >= 18 and hora <= 23:
        print('Boa noite!')

    else:
        print('Não conheço essa hora')
except:
    print('Você não digitou uma hora valida')



pegarNome = input('Digite seu nome: ')
tamanhoNome = len(pegarNome)

if tamanhoNome  > 1:

    if tamanhoNome <= 4:
        print('Nome Muito curto')

    elif tamanhoNome >= 5 and tamanhoNome <= 6:
        print('Seu nome é normal')

    else:
        print('Seu nome é muito grande')


else:
    print('nome não cadastrado')
