arquivo = open("dados.txt", "r")

conteudo = arquivo.readline()

print("tipo conteudo: ", type(conteudo))
print(repr(conteudo))

proximo_conteudo = arquivo.readline()

print("Próximo conteúdo retornado:")
print(repr(proximo_conteudo))

arquivo.close()