


# def multiplicarNum(a, b):
#     mutyiplica_a = a 
#     multiplica_b = b
#     multiplica = multiplica_b * mutyiplica_a
#     return multiplica
# resMulti = multiplicarNum(b=6, a=8)
# print(f'O resultado da multiplicação é "{resMulti}"') 



def ParOuImpar(par):
    if par % 2 == 0:
         return 'Par'
 
    return 'ímpar'
result = ParOuImpar(par=3)
print(result)





def multplicacao(*args):

    num = 1
    for numero in args:
        num *= numero
    return num

multplica = multplicacao(2,3,8)
print(multplica)

    