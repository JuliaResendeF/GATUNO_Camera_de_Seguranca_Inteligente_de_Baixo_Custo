import os
import webbrowser as web
import shutil

#Abre o web whatsapp para login
def Conect_Whats():
    web.open("https://web.whatsapp.com/")

#Abre a pasta de imagens
def OpenFolder_():
    dir_atual = os.path.dirname(os.path.abspath(__file__))
    img_folder_path = os.path.join(dir_atual, 'img')
    web.open(os.path.realpath(img_folder_path))

#Deletar todas as imagens da pasta imagens
def DelFolder_():
    dir_atual = os.path.dirname(os.path.abspath(__file__))
    img_folder_path = os.path.join(dir_atual, 'img')
    for item in os.listdir(img_folder_path):
        item_path = os.path.join(img_folder_path, item)
        if os.path.isdir(item_path):  
            shutil.rmtree(item_path)
    web.open(os.path.realpath(img_folder_path))    

