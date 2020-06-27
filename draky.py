import sys
import os
from gpiozero import CPUTemperature
import time
import socket
import random
import requests
memo1 = "0"
print("\033[91m                              ______________                               ")
print("\033[92m                        ,===:'.,            `-._                           ")
print("\033[93m                             `:.`---.__         `-._                       ")
print("\033[94m                               `:.     `--.         `.                     ")
print("\033[95m                                 \.        `.         `.                   ")
print("\033[96m                         (,,(,    \.         `.   ____,-`.,                ")
print("\033[97m                      (,'     `/   \.   ,--.___`.'                         ")
print("\033[98m                  ,  ,'  ,--.  `,   \.;'         `                         ")
print("\033[99m                   `{D, {    \  :    \;                                    ")
print("\033[91m                     V,,'    /  /    //                                    ")
print("\033[92m                     j;;    /  ,' ,-//.    ,---.      ,                    ")
print("\033[93m                     \;'   /  ,' /  _  \  /  _  \   ,'/                    ")
print("\033[94m                           \   `'  / \  `'  / \  `.' /                     ")
print("\033[91m                           `.___,'   `.__,'   `.__,'  ")
print("# PRIDE VERSION")
print("")
print("\033[91m[+]\033[97m Carregando Recursos")
time.sleep(.9)
print("\033[91m[+]\033[97m Iniciando Drakys-OS")
time.sleep(.5)
print(chr(27)+'[2j')
print('\033c')
print('\x1bc')
print("\033[91m")
print(" Draks \033[97m|\033[91m Pride Version")
for x in range(9000):

 res = input("\033[91m[+]\033[97m: \033[97m")
 if res == "clear":
  print(chr(27)+'[2j')
  print('\033c')
  print('\x1bc')
 if res == "reboot":
  print(chr(27)+'[2j')
  print('\033c')
  print('\x1bc')
  print("\033[91m[+]\033[97m Rebooting...")
  time.sleep(.2)
  os.system("python3 drak.py")
 if res == "sys":
  

  print('\033[97m Created By HydeDev')
  print('\033[97m Baseado em Python 3.7')
  print('\033[91m 1.2 \033[97m | \033[92mBETA')
 if res == "echo":
  res = input("\033[92m ")
 if res == "ping":
  pop1 = input("\033[97m ")
  print('\033[92m #Use CTRL+C to stop! \033[97m')
  os.system("ping " + str(pop1))
 if res == "py3":
  pop1 = input("\033[97m ")
  os.system("python3 " + str(pop1))
 if res == "dir":
	 
  os.system("dir")
 if res == "admin":
  pop1 = input("\033[97m ")
  os.system(pop1)
 if res == "date":
  os.system("date")
 if res == "netconfig":
  os.system("ifconfig")
 if res == "set memory1":
  print('\033[91m[+]\033[97m \033[91m 2,5 Kb \033[97m/\033[92m 10 Kb')
  memo1 = input('\033[97m ') 
 if res == "print memory1":
  
  print('\033[91m[+]\033[97m ' + memo1)	 
  
  


 if res == "get":
  url = input('\033[91m[+]\033[97m Download-URL: \033[97m')
  fileName = input('\033[91m[+]\033[97m FileName: \033[97m')
  print("\033[91m[+]\033[97m Baixando...")

  req = requests.get(url)
  file = open("get.crypt", 'wb')
  for chunk in req.iter_content(100000):
   file.write(chunk)
  file.close()
  print("\033[91m[+]\033[97m Criptografando Arquivo")
  time.sleep(.9)
  print("\033[91m[+]\033[97m Finalizando Arquivo")
  os.rename(r'get.crypt',fileName)
  time.sleep(.5)
  print("\033[91m[+]\033[97m Arquivo Baixado")

