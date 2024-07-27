def computeVendas():
    vendasList = []
    while True:
        number = input("Digite um número ou '[F]im' para terminar: ")
        
        if number.upper() == 'F':
            break
        
        try:
            number = int(number)
            if number == 0 and vendasList:
                vendasList.pop() 
            elif number != 0:
                vendasList.append(number)
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro ou '[F]' para finalizar o programa.")
    
    total_vendas = sum(vendasList)
    print(f"O total das vendas é: {total_vendas}")

computeVendas()