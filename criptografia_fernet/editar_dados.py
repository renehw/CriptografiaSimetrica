
from descriptografar_dados import DescriptografarDados

class EditarDados:
    teste = DescriptografarDados()
    
    file = open('../dadosCripto.text', 'rb')
    dadosCriptografados = file.read()
    file.close
    
    dados = teste.descriptografar(dadosCriptografados)
    print(dados)