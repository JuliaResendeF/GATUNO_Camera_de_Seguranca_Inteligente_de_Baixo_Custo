from customtkinter import *
from CTkMessagebox import CTkMessagebox
from PIL import Image, ImageTk
import Save_Settings as Save
import Teste_Func as TF
import Config as Conf
import Monitoramento as Moni

app = CTk()
app.geometry("856x645")


current_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(current_dir, "Image_Back.png")

set_appearance_mode("dark")
tabview_font = ("Arial", 20, 'bold')
tabview_config_font = ("Arial", 18, 'bold')
#image = Image.open(image_path)

my_image = CTkImage(Image.open(image_path),size=(350,250)) 
#Iniciar Monitoramento
def ShowVideo():
    msg = CTkMessagebox(title="Iniciar Monitoramento", message="Verifique se:\n \no IP da câmera já foi inserido\n\n A Câmera está ligada\n\nO Número de telefone já foi inserido\n\n A conexão com o Web WhatsApp já foi realizada\n\nO computador está conectado a internet\n\nAtenção: Clique no X da aba para encerrar o monitoramento\n\nA Câmera pode demorar alguns segundos para iniciar",                        icon="warning",option_1="Prosseguir", option_2="Cancelar")
    response = msg.get()
    if response=="Prosseguir":
      Moni.Iniciar_Monitoramento()
#Teste de imagem
def ShowImgTest():
    msg = CTkMessagebox(title="Teste de imagem", message="Verifique se:\n \no IP da câmera já foi inserido\n\n A Câmera está ligada\n\nO computador está conectado à internet\n\nAtenção: Clique no X da aba para encerrar o teste",                        icon="warning",option_1="Prosseguir", option_2="Cancelar")
    response = msg.get()
    if response=="Prosseguir":
        TF.Test_Mov() 
#Teste de Monitoramento
def ShowMonTest():
    msg = CTkMessagebox(title="Teste de Monitoramento", message="Verifique se:\n \no IP da câmera já foi inserido\n \n A Câmera está ligada\n\nO computador está conectado a internet\n\nAtenção: Clique no X da aba para encerrar o teste",
                        icon="warning",option_1="Prosseguir", option_2="Cancelar")
    response = msg.get()
    if response=="Prosseguir":
        TF.Test_Moni()
#Teste de Envio de mensagem
def ShowSendTest():
    msg = CTkMessagebox(title="Teste de Envio", message="Verifique se:\n \nO Número de telefone já foi inserido\n\n A conexão com o Web WhatsApp já foi realizada \n  \nO computador está conectado à internet  \n \nAtenção: Não mexa no Mouse durante o envio automatizado",                        icon="warning",option_1="Prosseguir", option_2="Cancelar")
    response = msg.get()

    if response=="Prosseguir":
        TF.Test_Mensage()      
#Abrir pasta de imagens     
def OpenFolder():
     Conf.OpenFolder_()
#Deletar todas as imagens    
def DelFolder():
     Conf.DelFolder_()
#Inserir IP da camera     
def IPSend():
    msg = CTkMessagebox(title="Inserir IP", message="Verifique se:\n\nA configuração da câmera já foi feita no Arduino IDE\n\nSe você já possui o número de IP da câmera\n\nAtenção: O IP deve ser inserido sem espaços no formato xxx.xxx.xx.xx\n\n Exemplo: 198.138.10.33",                        icon="warning",option_1="Prosseguir", option_2="Cancelar")
    response = msg.get()

    if response=="Prosseguir":
     dialog = CTkInputDialog(text="Digite o IP:", title="Inserir IP")
     Ip_CAM = dialog.get_input()
     if Ip_CAM is not None:
       Save.SaveIP(Ip_CAM)

#Inserir ou Alterar Numero de telefone           
def TelNumber():
    msg = CTkMessagebox(title="Inserir Telefone", message="\n\nEste número de telefone será usado para o envio das imagens capturadas\n\nAtenção: O número de telefone deve ser inserido sem espaços e com DDD no formato XXXXXXXXXXX\n\n Exemplo: 19111122333\n\n O número inserido pode ser o mesmo que foi usado para conectar o Web WhatsApp ou pode ser um número diferente",
                        icon="warning",option_1="Prosseguir", option_2="Cancelar")
    response = msg.get()
 
    if response=="Prosseguir":
     dialog = CTkInputDialog(text="Digite o Telefone:", title="Inserir Telefone")
     tel_send = dialog.get_input()
     if tel_send  is not None:
       Save.SaveTel(tel_send)    
#Conectar WhatsApp ao navegador
def ConeWhats():
        
    msg = CTkMessagebox(title="Conectar WhatsApp", message="\nEscaneie o Código QR com o aplicativo WhatsApp para conectar\n \nCaso ele ja esteja conectado, desconsidere este teste",icon="warning",option_1="Prosseguir", option_2="Cancelar")
    response = msg.get()

    if response=="Prosseguir":
        Conf.Conect_Whats() 

tabview = CTkTabview(master=app,width=800, height=600,corner_radius=20, 
                     segmented_button_selected_color="Gray",segmented_button_selected_hover_color="Gray",
                     state = "normal")
tabview.pack(padx=20, pady=20)

tabview._segmented_button.configure(font=tabview_font)

tabview.add("Iniciar")
tabview.add("Configuração")
tabview.add("Testes")


label_Iniciar= CTkLabel(master=tabview.tab("Iniciar"), text = "IP: "+ Save.ShowIP()+ "\n\n" +"Contato: "+Save.ShowTel()+"\n\n"+"\n\n", compound='bottom',image=my_image )
CTkButton(master=tabview.tab("Iniciar"), text="Iniciar Monitoramento",command=ShowVideo, fg_color="grey31",width=200, font=("Arial Bold", 30),hover_color="Gray").pack(anchor="center", ipady=5, pady=(60, 0))
label_Iniciar.pack(padx=20, pady=20)

CTkButton(master=tabview.tab("Testes"), text="Imagem",command=ShowImgTest, fg_color="grey31",width=200, font=("Arial Bold", 30),hover_color="Gray").pack(anchor="center", ipady=5, pady=(60, 0))
label_Iniciar.pack(padx=20, pady=20)

CTkButton(master=tabview.tab("Testes"), text="Monitoramento",command=ShowMonTest, fg_color="grey31",width=200, font=("Arial Bold", 30),hover_color="Gray").pack(anchor="center", ipady=5, pady=(60, 0))
label_Iniciar.pack(padx=20, pady=20)

CTkButton(master=tabview.tab("Testes"), text="Envio de mensagens",command=ShowSendTest, fg_color="grey31",width=200, font=("Arial Bold", 30),hover_color="Gray").pack(anchor="center", ipady=5, pady=(60, 0))
label_Iniciar.pack(padx=20, pady=20)

tabview_config = CTkTabview(master=tabview.tab("Configuração"),width=600, height=600,corner_radius=30, 
                     segmented_button_selected_color="Gray",segmented_button_selected_hover_color="Gray", 
                     fg_color="grey21",      
                     state = "normal")
tabview_config.pack(padx=20, pady=20)

tabview_config.add("Configuração Geral")
tabview_config.add("Configuração Inicial")

CTkButton(master=tabview_config.tab("Configuração Geral"), text="Abrir pasta de imagens",command=OpenFolder, fg_color="grey31",width=200, font=("Arial Bold", 30),hover_color="Gray").pack(anchor="center", ipady=5, pady=(60, 0))
label_Iniciar.pack(padx=20, pady=20)

CTkButton(master=tabview_config.tab("Configuração Geral"), text="Excluir todas as imagens",command=DelFolder, fg_color="grey31",width=200, font=("Arial Bold", 30),hover_color="Gray").pack(anchor="center", ipady=5, pady=(60, 0))
label_Iniciar.pack(padx=20, pady=20)

CTkButton(master=tabview_config.tab("Configuração Inicial"), text="IP da Câmera",command=IPSend, fg_color="grey31",width=200, font=("Arial Bold", 30),hover_color="Gray").pack(anchor="center", ipady=5, pady=(60, 0))
label_Iniciar.pack(padx=20, pady=20)

CTkButton(master=tabview_config.tab("Configuração Inicial"), text="Registrar/Alterar número de telefone",command=TelNumber, fg_color="grey31",width=200, font=("Arial Bold", 30),hover_color="Gray").pack(anchor="center", ipady=5, pady=(60, 0))
label_Iniciar.pack(padx=20, pady=20)

CTkButton(master=tabview_config.tab("Configuração Inicial"), text="Conectar WhatsApp",command=ConeWhats, fg_color="grey31",width=200, font=("Arial Bold", 30),hover_color="Gray").pack(anchor="center", ipady=5, pady=(60, 0))
label_Iniciar.pack(padx=20, pady=20)

tabview_config._segmented_button.configure(font=tabview_config_font)

app.mainloop()
