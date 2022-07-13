import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


class Cifrador:
    def __init__(self):
        pass
    
    
    def criptografar(self,key):
      
       # key = os.urandom(32)  #substituir por chave lida do arquivo       
        iv = os.urandom(16)   #gera numero aleatorio de 16 bytes
        cipher = Cipher(algorithms.AES(key), modes.CBC(b"\x00" * 16))
        encryptor = cipher.encryptor()
        ct = encryptor.update(b"a secret message") + encryptor.finalize()
        return ct
    
    
