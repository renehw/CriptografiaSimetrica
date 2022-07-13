from cryptography.fernet import Fernet

class CriptografarDados:
    def __init__(self) -> None:
        pass
    
    def criptografar():
        file = open('../chave.key', 'rb')
        chave = file.read()
        file.close
        print("\n\n")
        print(chave)

        f = Fernet(chave)
        
        dadosCriptografados = f.encrypt(b"Felipe e mala")

        file = open('../dadosCripto.text', 'wb')
        file.write(dadosCriptografados)
        file.close
        
        print(f'Dados Criptografados: {dadosCriptografados}')
        
    criptografar()
        
        
    
    
    
    