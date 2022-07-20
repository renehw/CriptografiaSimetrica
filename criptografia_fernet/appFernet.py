from criptografar_dados_fernet import CriptografarDados
from descriptografar_dados import DescriptografarDados
from editar_dados import EditarDados
from gerar_chave import GenerateKey

def appFernet():
    gerarChave =  GenerateKey()
    encript = CriptografarDados()
    descript = DescriptografarDados()
    edit = EditarDados()
    
    gerarChave.gerarChave()
    
    texto = input('Texto a ser crifrado: ')
    
    textoCriptografado = encript.criptografar(texto)
    print(f'\nTexto Criptografado: ' + str(textoCriptografado, 'utf-8'))
    editarDados = edit.editarDados()
    print(f'Texto Descriptografado: ' + str(editarDados, 'utf-8'))
    newText = input(f'Editar: ')
    novoTextoCriptografado = encript.criptografar(f'{editarDados} {newText}')
    print(f'\nTexto editado Criptografado: ' + str(novoTextoCriptografado, 'utf-8'))
    textoDescriptogragafado = descript.descriptografar(novoTextoCriptografado)
    print(f'Texto editado Descriptografado: ' + str(textoDescriptogragafado, 'utf-8'))
    
    
appFernet()
    