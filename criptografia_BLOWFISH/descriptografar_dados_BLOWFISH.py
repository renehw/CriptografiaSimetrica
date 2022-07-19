import os
from statistics import mode
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


class Decifrador:
    def __init__(self):
        pass
    
    
    def decryptografar(self,textoCriptografado,key):
            
            cipher = Cipher(algorithms.Blowfish(key), modes.CBC(b"\x00" * 8))
            decryptor = cipher.decryptor()
            decryp = decryptor.update(textoCriptografado) + decryptor.finalize()
            decryp = decryp.replace(b'\x00', b'')
            return decryp