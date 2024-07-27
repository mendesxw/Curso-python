

palavra = 'lucas'
metodo = 'upper'

# palavra.islower

if hasattr(palavra, metodo):
    result_metodo = getattr(palavra, metodo)()
    print(result_metodo)

else:
    print('Result undefind')


