from cryptography.fernet import Fernet

class GenerateKey:
    def __init__(self) -> None:
        pass
    
    def gerarChave(self):
        try:
            chave = Fernet.generate_key()
            file = open('chave.key', 'wb')
            file.write(chave)
            file.close
            print('Chave gravada com sucesso')
        except:
            print('Não foi possivel gravar sua chave, tente novamente.')
