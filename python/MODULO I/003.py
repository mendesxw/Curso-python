

nomeAluno = input("Seu Nome: ")



mediaPrimeiroSem = int(input("Olá, " + nomeAluno + " Digite sua média do segundo semeste: "))
mediasegundoSem = int(input("Olá, " + nomeAluno +" Digite Sua mádia do segundo semestre: "))
mediaTerceiroSem = int( input("Olá, " + nomeAluno +" Digite sua média do terciro semestre: "))
mediaQuartoSem = int(input("Olá, " + nomeAluno +" Digite sua média do quarto semestre: "))

result = (mediaPrimeiroSem + mediasegundoSem + mediaTerceiroSem + mediaQuartoSem) / 4
print(result)

if result > 5:
     print("O aluno " + nomeAluno + " está em situação final aprovado!")

else:
     print("O(a) aluno (a) " +nomeAluno+", está em situação final reprovado!")