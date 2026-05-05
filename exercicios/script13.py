with open ("dados12.txt" , "r") as arquivo:
    print("Total de Linhas no arquivo:")
    contador = 0
    for linha in arquivo:
        if linha:
            contador += 1
            print("total = " , contador)
            