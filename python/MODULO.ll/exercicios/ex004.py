
sistema_de_perguntas = [
    {
        'pergunta': 'Quel descobriu o Brasil?',
        'opicao': [
            'Pedro Alvares Cabral',
            'Cristiano Ronaldo', 
            'Vasco da Gama',
            'Lula',
            'Bolsonaro'
        ],

        'resposta': 'Pedro Alvares Cabral'
    },

    {
        'pergunta': 'Qual das tecnologias abaixo nao é uma linguagem de programação?',
        'opicao': [
            'Java',
            'JavaScript', 
            'C++',
            'Ruby',
            'HTML'
        ],

        'resposta': 'HTML'

    },

    {
     
      'pergunta':'Qual continente fica localizado o Brasil?',

      'opicao': [
          'Àfrica',
          'Europa',
          'Ásia', 
          'Oceania',
          'América'
      ],
      'resposta': 'América'
    }
     
]

qtd_opcoes = 0
for pergunta in sistema_de_perguntas:
    print('Pergunta',pergunta['pergunta'])
    print()

    opicoes_de_resposta = pergunta['opicao']

    for i , opicoes in enumerate('opico'):
     print(f'{i})' )
     print()

    fazer_a_escolha_da_resposta = input('Escolha uma opição: ')

    acertou = False
    escolha_int = None
    qtd_opcoes = len(opicoes)


    if fazer_a_escolha_da_resposta.isdigit():
     escolha_int = int(fazer_a_escolha_da_resposta)

    if escolha_int < 0 and escolha_int < qtd_opcoes:
      if opicoes[escolha_int] == pergunta['pergunta']:
        acertou = True

    print()

    if acertou:
      qtd_opcoes+=1
      print('Acertou 👍')

    else:
      print('Errou ❌')

    print()

print(f'Você acertou {qtd_opcoes}')
print(f'de {len(sistema_de_perguntas)} perguntas')





