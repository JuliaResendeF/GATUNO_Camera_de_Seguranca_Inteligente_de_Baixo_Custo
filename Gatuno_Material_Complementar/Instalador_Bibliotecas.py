import subprocess
import sys

request =['pywhatkit','customtkinter','CTkMessagebox','opencv-python','pywin32']

for i in request:
                subprocess.check_call([sys.executable, "-m", "pip", "install", i])


# bibliotecas 

# instalar 
# pywhatkit
# customtkinter
# CTkMessagebox
# opencv-python
# pywin32

# não instalar
# time
# os
# PIL
# webbrowser
