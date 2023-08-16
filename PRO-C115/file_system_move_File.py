import os

# Caminho do arquivo de origem
source = 'main.txt'

# Novo nome desejado para o arquivo
dest = "newfile.txt"

# Caminho completo para o arquivo de destino com o novo nome
dest = os.path.join(os.path.dirname(source), dest)

# Renomear o arquivo
os.rename(source, dest)

print("O caminho de origem foi renomeado para o caminho de destino com sucesso.")


