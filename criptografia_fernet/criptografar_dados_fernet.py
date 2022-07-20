from cryptography.fernet import Fernet

class CriptografarDados:
    def __init__(self) -> None:
        pass
    
    def criptografar(self, texto):
        file = open('chave.key', 'rb')
        chave = file.read()
        file.close

        f = Fernet(chave)
        b = bytes(texto, 'utf-8')
        dadosCriptografados = f.encrypt(b)

        file = open('dadosCripto.text', 'wb')
        file.write(dadosCriptografados)
        file.close
        
        return dadosCriptografados
    