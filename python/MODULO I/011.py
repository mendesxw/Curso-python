"""
Operação ternaria nada mais é que um (if else) em uma unica linha.
ela fem a mesma funcionalidade que os mesmos e pode ser usada quando a verificação das mesmas é algo considerado 'simples'

"""

# exx: 

estudantesIemaCentro = 40 
estudantesIemaAnil = 80
condicao = estudantesIemaAnil < estudantesIemaCentro
resultado = estudantesIemaAnil if condicao else estudantesIemaCentro

print(f'A instituição Iema Rio Anil contém {resultado} estudantes  ')

'''
Também escrevemos este código de outra forma: 
'''

if estudantesIemaCentro > estudantesIemaAnil: 
    print(f'A instituição Iema Rio Anil tem {estudantesIemaAnil} alunos')

else: 
    print(f'A instituição Iema Centro contém {estudantesIemaCentro} alunos')