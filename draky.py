import sys
import os
import time
import socket
import random
import requests
print("\033[91m")
print("                              ______________                               ")
print("                        ,===:'.,            `-._                           ")
print("                             `:.`---.__         `-._                       ")
print("                               `:.     `--.         `.                     ")
print("                                 \.        `.         `.                   ")
print("                         (,,(,    \.         `.   ____,-`.,                ")
print("                      (,'     `/   \.   ,--.___`.'                         ")
print("                  ,  ,'  ,--.  `,   \.;'         `                         ")
print("                   `{D, {    \  :    \;                                    ")
print("                     V,,'    /  /    //                                    ")
print("                     j;;    /  ,' ,-//.    ,---.      ,                    ")
print("                     \;'   /  ,' /  _  \  /  _  \   ,'/                    ")
print("                           \   `'  / \  `'  / \  `.' /                     ")
print("                           `.___,'   `.__,'   `.__,'  ")
print("")
print("\033[91m[+]\033[97m Carregando Recursos")
time.sleep(.5)
print(chr(27)+'[2j')
print('\033c')
print('\x1bc')
print("\033[91m[+]\033[97m Iniciando Drakys-OS")
time.sleep(.5)
print(chr(27)+'[2j')
print('\033c')
print('\x1bc')
for x in range(9000):
 res = input("\033[96m[+]\033[91m: \033[97m")
 if res == "clear":
  print(chr(27)+'[2j')
  print('\033c')
  print('\x1bc')
 if res == "echo":
  res = input("\033[96m[+]\033[91mEcho: \033[97m ")
  print(res)
 if res == "get":
  url = input('\033[91m[+]\033[96m Download-URL: \033[97m')
  fileName = input('\033[91m[+]\033[96m FileName: \033[97m')
  print("\033[91m[+]\033[96m Baixando...")

  req = requests.get(url)
  file = open("get.crypt", 'wb')
  for chunk in req.iter_content(100000):
   file.write(chunk)
  file.close()
  print("\033[91m[+]\033[97m Criptografando Arquivo")
  time.sleep(.9)
  print("\033[91m[+]\033[97m Baixando Arquivo")
  os.rename(r'get.crypt',fileName)
  time.sleep(.5)
  print("\033[91m[+]\033[97m Arquivo Baixado")
