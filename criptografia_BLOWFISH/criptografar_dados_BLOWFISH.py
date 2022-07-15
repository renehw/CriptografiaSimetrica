import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from Crypto.Cipher import Blowfish


class Cifrador:
    def __init__(self):
        pass
    
    
    def criptografar(self):
        key = os.urandom(32)  #substituir por chave lida do arquivo  
        file = open('BLOWFISH.key', 'wb')
        file.write(key)
        file.close     
        
        cipher = Cipher(algorithms.Blowfish(key), modes.CBC(b"\x00" * 8))
        encryptor = cipher.encryptor()
        
        ct = encryptor.update(b"a secret mensage") + encryptor.finalize()
        file = open('BLOWFISH-content.txt','wb')
        file.write(ct)
        file.close
        return ct
    
    
    
    
