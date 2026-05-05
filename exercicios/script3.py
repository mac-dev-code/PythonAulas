arquivo = open("dados.txt")

conteudo = arquivo.readline()

print("tipo do conteudo:", type(conteudo))

print("Conteudo retornado pelo readline:")
print(repr(conteudo))

proximo_conteudo = arquivo.readline()

print("Proximo conteudo retornado:")
print(repr(proximo_conteudo))

arquivo.close()