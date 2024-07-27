
import os 
lista = []

while True:

    perguntaUser = input('[I]nserir [A]pagar [l]istar: ')

    if perguntaUser == 'I':
        os.system('cls')
        valor = input('Valor: ')
        lista.append(valor)
    elif perguntaUser == 'A':
        os.system('cls')
        indice_delet = input('escolha um indice para apagar: ')

        try:
            indice =  int(indice_delet)
            del lista[indice]

        except ValueError:
           print('Por favor digite número int.')
        except IndexError:
           print('Índice não existe na lista')
        except Exception:
           print('Erro desconhecido')

    elif perguntaUser == 'l':
        os.system('cls') 

        if len(lista) == 0:
            print('nada para listar')

        for i, valor in enumerate(lista):
            print(i, valor)

    else:
        print('Por favor, escolha i, a ou l.')



    