from cryptography.fernet import Fernet

class CriptografarDados:    
    file = open('chave.key', 'rb')
    chave = file.read()
    file.close
    print(chave)

    dados = 'Este é um texto criptografado simetricamente'
    f = Fernet(chave)

    dadosCriptografados = f.encrypt(b"Este e um texto criptografado simetricamente")
    print(f'{dadosCriptografados}') 