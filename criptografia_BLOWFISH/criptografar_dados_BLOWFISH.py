import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


class Cifrador:
    def __init__(self):
        pass
    
    
    def criptografar(self,texto):
        key = os.urandom(32)  #substituir por chave lida do arquivo  
        file = open('BLOWFISH.key', 'wb')
        file.write(key)
        file.close     
        
        tamanho = len(texto)
        
        
        cipher = Cipher(algorithms.Blowfish(key), modes.CBC(b"\x00" * 8))
        encryptor = cipher.encryptor()
        while tamanho % 8 != 0:
            texto += b"\x00"
            tamanho += 1
        
        
        ct = encryptor.update(texto) + encryptor.finalize()
        file = open('BLOWFISH-content.txt','wb')
        file.write(ct)
        file.close
        return ct

    
    
    
