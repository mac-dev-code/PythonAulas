arquivo = open('dados.txt', 'r')

conteudo = arquivo.read()
print("Todo o conteudo do arquivo")
print(repr(conteudo), '\n')

conteudo_releitura = arquivo.read()
print("Releitura de todo o conteudo do arquivo")
print(repr(conteudo_releitura), '\n')

arquivo.close()

arquivo_reaberto = open('dados.txt', 'r')

conteudo_reaberto = arquivo_reaberto.read()
print("todo o conteudo do arquivo novamente")
print(repr(conteudo_reaberto), '\n')

arquivo_reaberto.seek(8)
conteudo_seek = arquivo_reaberto.read()
print("Todo o conteudo do arquivo após o seek")
print(repr(conteudo_seek), '\n')

arquivo_reaberto.close()
