import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


class Cifrador:
    def __init__(self):
        pass
    
    
    def criptografar(self):
        key = os.urandom(32)  #substituir por chave lida do arquivo  
        file = open('AES.key', 'wb')
        file.write(key)
        file.close     
       
        cipher = Cipher(algorithms.AES(key), modes.CBC(b"\x00" * 16))
        encryptor = cipher.encryptor()
        ct = encryptor.update(b"a secret mensage") + encryptor.finalize()
        file = open('AES-content.txt','wb')
        file.write(ct)
        file.close
        return ct
    
    
