from criptografar_dados_BLOWFISH import Cifrador
from descriptografar_dados_BLOWFISH import Decifrador

def lerChave():
    file = open('BLOWFISH.key', 'rb')
    return file.readlines()

def lerConteudo():
    file = open('BLOWFISH-content.txt', 'rb')
    return file.readlines()
    

def criptografar():
    cypher = Cifrador()
    textocripto = cypher.criptografar() 
    print("\n\n")
    print("Texto Criptografado: ")
    print(textocripto)
    return textocripto
    
def decryptografar(textocripto,key):
    decypher = Decifrador()
    print("Chave: ")
    print(key)
    textoPuro= decypher.decryptografar(textocripto,key)
    print("Texto Descriptografado")
    print(textoPuro)

# inicio 
criptografar() #gera um novo arquivo cifrado e uma nova chave
# comentar funcao acima para utilizar a mesma chave para decifrar

criptoList = lerConteudo()
textoCripto = criptoList[0]

chaveList = lerChave()
key = chaveList[0]

decryptografar(textoCripto,key)





     