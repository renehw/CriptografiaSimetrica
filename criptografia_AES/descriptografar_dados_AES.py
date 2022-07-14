import os
from statistics import mode
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


class Decifrador:
    def __init__(self):
        pass
    
    
    def decryptografar(self,textoCriptografado,key):
            
            cipher = Cipher(algorithms.AES(key), modes.CBC(b"\x00" * 16))
            decryptor = cipher.decryptor()
            decryp = decryptor.update(textoCriptografado) + decryptor.finalize()
            return decryp