import cv2
import os
import time
from Mensage_Send import SendMensage
import Save_Settings as Save


def Iniciar_Monitoramento():
#Retorna o tempo atual (dia_mes_ano) para o nome da pasta utilizada
 time_now_folder= time.localtime()
 time_format_folder = time.strftime("%d_%m_%Y", time_now_folder)

#Recebe a pasta em que o arquivo python está
 dir_atual = os.path.dirname(os.path.abspath(__file__))
#Recebe a pasta em que as imagens são armazenadas (\img)
 img_folder_path = os.path.join(dir_atual, 'img')
#Recebe a pasta em que as imagens salvas do dia de execução do arquivo serão armazenadas (dia_mes_ano)
 today_folder_path = os.path.join(img_folder_path, time_format_folder)
#Verifica se já existe uma pasta com o dia de execução do arquivo, caso ela não exista, ela será criada
 if not os.path.exists(today_folder_path):
    os.makedirs(today_folder_path)


 

 def connect_video():
    #Reconecta a camera com o software
    global video
    video.release()  
    video = cv2.VideoCapture(Save.ShowIP())

 def Monitoramento_On():
        global video
        
        #Inicia a captura das imagens da câmera usando o IP da câmera inserido na interface
        video = cv2.VideoCapture(Save.ShowIP())
        verifica, img_2 = video.read()
        #verifica a conexão da camera
        if not verifica:
         #Se não estiver conectado, ele inicia a função connect_video()
         print("Reconectando")
         connect_video()
         return

        #Coverte a 1° imagem para a escala preto e branco
        Gray1 = cv2.cvtColor(img_2, cv2.COLOR_BGR2GRAY)

        Print_Cont = 0
        #Inicializa a contagem de imagens salvas, garante que mais de uma imagem tenha o mesmo nome (mais detalhes mais abaixo no codigo)
        #Print_Cont = 0
        while True:
            #Define como False a variavel que verifica se uma imagem deve(True) ou não(False) ser salva
            Print = False
            #Inicia a leitura das imagens da camera
            verifica, img = video.read()

            if not verifica:
             print("Reconectando")
             connect_video()
             continue 
            #Coverte a 2° imagem para a escala preto e branco
            Gray2 = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)

            #Calcula a diferença absoluta entre as duas imagens
            Cruzamento_img = cv2.absdiff(Gray1, Gray2)

            #Delimita os pixels das imagens em 2 categorias (preto e branco)
            _, Barreira_detec = cv2.threshold(Cruzamento_img, 30, 255, cv2.THRESH_BINARY)
           
            #Detecta os contornos na imagem
            Limitar_area, _ = cv2.findContours(Barreira_detec, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            
            #Forma o contorno em volta do movimento detectado (Uma forma retangular)
            for Limitar_area in Limitar_area:

                if cv2.contourArea(Limitar_area) > 1000:
                    a, b, c, d = cv2.boundingRect(Limitar_area)
                    cv2.rectangle(img, (a, b), (a+c, b+d), (0, 255, 255), 2)

                    #Define como False a variavel que verifica se uma imagem se uma imagem deve ser salva
                    Print = True   

            #Exibe a imagem da camera com o monitoramento sendo realizado
            cv2.imshow('Monitoramento', img)
            if Print == True:
                #Recupera o tempo atual para colocar no nome da imagem salva
                time_now = time.localtime()
                time_format = time.strftime("%d_%m_%Y__%H.%M.%S_", time_now)

                #Adiciona +1 toda vez que uma imagem é salva para garantir que todas as imagens tenham nomes diferentes e nenhum erro de salvamento ocorra
                Print_Cont = Print_Cont + 1
                #Transfoma a variavel Print_Cont em string para que sejam adicionada ao nome da imagem salva
                Print_Cont_used = str(Print_Cont)
                #Junta o tempo atual + o contador de imagens salvas + "_Image" + a extensão do arquivo (.png)
                name_file = time_format + Print_Cont_used + "_Image.png"
                
                #Define o caminho em que a imagem sera salva (pasta do dia atual, nome da pasta)
                caminho_print = os.path.join(today_folder_path, name_file)
                #Salva a imagem
                cv2.imwrite(caminho_print, img)

                #Manda o dia atual (nome da pasta onde a imagem foi salva) e o nome da imagem para a função que enviara as mensagens 
                SendMensage(time_format_folder,name_file)
                #print("Print capturado e salvo em:", caminho_print) (Usado para testes)  
                

            

        #Finaliza o loop e a captura das imagens da câmera após clicar no X da aba
            if cv2.waitKey(1) & 0xFF == ord('q'):
                   break       
            if cv2.getWindowProperty('Monitoramento', cv2.WND_PROP_VISIBLE) < 1:
                break 

        video.release()
        if cv2.getWindowProperty('Monitoramento', cv2.WND_PROP_VISIBLE) >= 1:
         cv2.destroyWindow('Monitoramento')

        cv2.destroyAllWindows()        
 Monitoramento_On()           