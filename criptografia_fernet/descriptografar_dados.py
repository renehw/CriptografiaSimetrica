from cryptography.fernet import Fernet

class DescriptografarDados:
    def __init__(self) -> None:
        pass
    
    def descriptografar(self, dadosCriptografados):
        file = open('../chave.key', 'rb')
        chave = file.read()
        file.close
        
        f = Fernet(chave)
        dadosDescriptografados = f.decrypt(dadosCriptografados)

        file = open('../dadosDescripto.text', 'wb')
        file.write(dadosDescriptografados)
        file.close
        
        return dadosDescriptografados