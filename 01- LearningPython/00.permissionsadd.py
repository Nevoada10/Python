import os

# Caminho da pasta que deseja alterar as permissões
pasta = "/Users/urielnevessilva/Desktop/Programing/Python/35moveafiletest"

# Permissões completas (rwx) para o proprietário, grupo e outros usuários
permissao = 0o777

# Altera as permissões da pasta
os.chmod(pasta, permissao)
