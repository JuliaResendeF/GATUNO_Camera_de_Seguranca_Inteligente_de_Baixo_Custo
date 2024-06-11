import os
#import ast

#Pasta do projeto e pasta dos arquivos txt
script_dir = os.path.dirname(os.path.abspath(__file__))
save_folder_path = os.path.join(script_dir, 'SaveSettings')

IP_Cam = os.path.join(save_folder_path, 'IP_Cam.txt')
Tel_Number= os.path.join(save_folder_path, 'Tel_Number.txt')

#Salvar IP inserido no arquivo.txt
def SaveIP(IP_Number):
    IP_Number ="http://"+IP_Number+":81/stream"
    with open(IP_Cam , 'w') as arquivo:
         arquivo.write(str(IP_Number))
         
#Recuperar o numero de Ip
def ShowIP():
   with open(IP_Cam, 'r') as arquivo:
        linha = arquivo.read()
        return linha

#Salvar Numero de telefone inserido no arquivo.txt
def SaveTel(Tel_Num):
    Tel_Num = "+"+Tel_Num 
    with open(Tel_Number , 'w') as arquivo:
         arquivo.write(str(Tel_Num))
         
#Recuperar o numero de telefone
def ShowTel():
  with open(Tel_Number, 'r') as arquivo:
        linha = arquivo.read()
        return linha