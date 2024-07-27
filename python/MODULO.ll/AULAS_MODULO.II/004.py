"""
148.
Nesta aula, vi sobre yeid from, importar funções atravez de um from.

Consigo fazer essa importação de uma forma apenas, e executo a função de três formas diferentes.

Exemplo:
"""

def contagem():
    yield 1
    yield 2
    yield 3

def contageImport():
    yield from contagem()
    yield 4
    yield 5
    yield 6

result = contageImport()
for NUMBER in result:
    print(NUMBER)   


print()
"""
ESSA FOI A PRIMEIRA FORMA. A SEGUNDA, É PASSANDO UM UM PARAMETRO PARA A FUNÇÃO E IMPORTAR O PARAMENTRO COMO UMA FUNÇÃO. PARA EXECUTAR, PASSO A PRIMEIRA FUNÇÃO COMO ARGUMENTO DA SEGUNDA {

            result = contageImport(contagem())

}

EXX:
"""

def contagem():
    yield 1
    yield 2
    yield 3

def contageImport(args):
    yield from args
    yield 4
    yield 5
    yield 6

result = contageImport(contagem())
for number in result:
    print(number)