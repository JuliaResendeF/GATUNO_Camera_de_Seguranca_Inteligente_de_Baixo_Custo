import pywhatkit as kit
import os
import Save_Settings as Save
from time import sleep



#dir_atual = os.path.dirname(os.path.abspath(__file__))
#img_folder_path = os.path.join(dir_atual, 'img')

def SendMensage(pasta_name,name_file): 
    #Retorna o numero de telefone
    number = Save.ShowTel()
    #retorna o nome da imagem
    nome_image = name_file
    #retorna pasta de imagens com nome do dia da execução
    dir_atual = os.path.dirname(os.path.abspath(__file__))
    img_folder_path = os.path.join(dir_atual, 'img')
    image_send = os.path.join(img_folder_path, pasta_name, nome_image)
    #Junta o nome da mensagem com um caption
    capition = "Um movimento foi Detectado! - " + nome_image 
    #Envia a mensagem
    kit.sendwhats_image(number,  image_send, capition,15, True)






