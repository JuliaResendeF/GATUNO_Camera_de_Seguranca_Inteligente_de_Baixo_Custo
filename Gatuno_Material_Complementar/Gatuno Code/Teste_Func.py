import pywhatkit as kit
import os
import cv2
import Save_Settings as Save

ip_cam = Save.ShowIP()


#Teste de envio de mensagem
def Test_Mensage():
    dir_atual = os.path.dirname(os.path.abspath(__file__))
    nome_image = "TesteMensagem.png"
    image_send = os.path.join(dir_atual, "Images", nome_image)
    number = Save.ShowTel()
    capition = 'Teste de camera'
    kit.sendwhats_image(number, image_send, capition,15, True)

#teste de imagem
def Test_Mov():
    video = cv2.VideoCapture(ip_cam)
    while True:
            verifica, frame = video.read()
            cv2.imshow("video", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                   break       
            if cv2.getWindowProperty('video', cv2.WND_PROP_VISIBLE) < 1:
                break
    video.release()
    if cv2.getWindowProperty('video', cv2.WND_PROP_VISIBLE) >= 1:
       cv2.destroyWindow('video')
    cv2.destroyAllWindows()  

#teste de monitoramento 
def Test_Moni():
        video = cv2.VideoCapture(ip_cam)
        verifica, img_2 = video.read()
        Img_cinza1 = cv2.cvtColor(img_2, cv2.COLOR_BGR2GRAY)
        Print_Cont = 0
        while True:
            #Inicia a leitura das imagens da camera
            verifica, img = video.read()
            Img_cinza2 = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
            Cruzamento_img = cv2.absdiff(Img_cinza1, Img_cinza2)

            Controle_, Barreira_detec = cv2.threshold(Cruzamento_img, 30, 255, cv2.THRESH_BINARY)

            Limitar_area, _ = cv2.findContours(Barreira_detec, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            
            for Limitar_area in Limitar_area:
                if cv2.contourArea(Limitar_area) > 1000:
                    A, B, C, D = cv2.boundingRect(Limitar_area)
                    cv2.rectangle(img, (A, B), (A+C, B+D), (0, 255, 255), 2) 

            #Exibe a imagem da camera com o monitoramento sendo realizado
            cv2.imshow('Monitoramento', img)
    
            if cv2.waitKey(1) & 0xFF == ord('q'):
                   break       

            if cv2.getWindowProperty('Monitoramento', cv2.WND_PROP_VISIBLE) < 1:
                break
            
        video.release()
        if cv2.getWindowProperty('Monitoramento', cv2.WND_PROP_VISIBLE) >= 1:
         cv2.destroyWindow('Monitoramento')
        cv2.destroyAllWindows() 