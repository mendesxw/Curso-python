
frase = 'A linguagem python, é uma linguagem de tipagem forte e sintaxe simples que foi criada pelo Holanês Guido van Rossum  um programador de computador na Holanda, criou o Python. Ele começou em 1989 no Centrum Wiskunde & Informatica (CWI), inicialmente como um projeto de hobby para se manter ocupado durante o Natal.'

i = 0
apareceuqtd = 0
pareceuVezesMais = ' '
while i < len(frase):
    letraPegar = frase[i]

    i += 1

    if letraPegar == ' ':
        i += 1
        continue

qtdAtual = frase.count(letraPegar)

if apareceuqtd < qtdAtual:
    apareceuqtd = qtdAtual
    pareceuVezesMais = letraPegar


i += 1


print(pareceuVezesMais )


    