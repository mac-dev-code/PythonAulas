arquivo = open('dados.txt')

print("Nome do arquivo", arquivo.name)
print("Modo do arquivo", arquivo.mode)
print("ler o arquivo:", arquivo.read())

arquivo.close()

print("Arquivo fechado?", arquivo.closed)
