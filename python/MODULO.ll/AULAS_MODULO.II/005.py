

"""
149.

Voltando um pouco nos conteudos, vi a continuação de try e except. Consegui ver um pouco de tratamentos de erros com except e a passagem de erros a serem tratados. 

Vi tambem que posso passar mais de um erro por vez utilizando uma tupla. 
EX:
"""

# numberOne = 10
# numberTwo = 0


# try:
#     result = numberOne / numberTwo
    
# except:
#     print('hello world!')


numberOne = 10
numberTwo = 0

try:
    tue = numberOne[32000]
    result = numberOne / numberTwo * tue
    print(tue)
except (ZeroDivisionError, TypeError):
    print('hello world!, TypeError')


