

def multplicaFunction(multiplicar):
   def multiplica(numero):
    return numero * multiplicar
   
   return multiplica


duplica = multplicaFunction(2)
print(duplica(2))


triplica = multplicaFunction(3)
print(triplica(3))
 

quadriplica = multplicaFunction(4)
print(quadriplica(4))