
"""
Generation functions, são funções que pausam. Ao invez 
utilizar o return, ela usa o yield. Mesmo assim, ela consegue receber um return após o yield. 

Esse return, só será atingido caso a função seja chamada muitas vezes ao ponto de não ter mais valores para execução. 

A generation function é considerada um iterator, então, é chamada utilizando a class __next__ ou next()

exemplo:
"""

def generation(n=50, max= 500):
#    while True:
    yield n
    #    n+=1

    #    if n > max:
    #        return "acabou"
       
result = generation()
print(next(result))
for n in result:
    print(n)

