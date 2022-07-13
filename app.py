from CriptografiaSimetrica.criptografar_dados_AES import Cifrador
from descriptografar_dados_AES import Decifrador

cypher = Cifrador()
decypher = Decifrador()

textocripto = cypher.criptografar(b"1234567890123456")

print(textocripto)
textoPuro= decypher.descriptografar(textocripto,b"1234567890123456")

print(textoPuro)