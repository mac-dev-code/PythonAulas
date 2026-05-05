with open("dados12.txt") as arquivo:
    print("Representação das linhas com strip:")
    for linha in arquivo:
        linha_limpa = linha.strip()
        print(repr(linha_limpa))