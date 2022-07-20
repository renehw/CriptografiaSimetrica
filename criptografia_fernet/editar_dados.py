
from descriptografar_dados import DescriptografarDados

class EditarDados:
    def __init__(self) -> None:
        pass
    
    def editarDados(self):
        teste = DescriptografarDados()
    
        file = open('dadosCripto.text', 'rb')
        dadosCriptografados = file.read()
        file.close
        
        dados = teste.descriptografar(dadosCriptografados)
        return dados