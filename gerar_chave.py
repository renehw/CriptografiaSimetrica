from cryptography.fernet import Fernet

chave = Fernet.generate_key()
print(chave)

file = open('chave.key', 'wb')
file.write(chave)
file.close

dados = 'Este é um texto criptografado simetricamente'
f = Fernet(chave)

dadosCriptografados = f.encrypt(b"Este e um texto criptografado simetricamente")
print(f'{dadosCriptografados}')

dadosDescriptografados = f.decrypt(dadosCriptografados)
print(dadosDescriptografados)