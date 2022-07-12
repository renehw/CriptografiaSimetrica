from cryptography.fernet import Fernet

chave = Fernet.generate_key()
print(chave)

file = open('chave.key', 'wb')
file.write(chave)
file.close

# dadosDescriptografados = f.decrypt(dadosCriptografados)
# print(dadosDescriptografados)