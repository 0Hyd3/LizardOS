import sys
import os
from gpiozero import CPUTemperature
import time
import socket
import random
import requests

memo1 = "0"
memo2 = "1"
memo3 = "2"
curso = ">"
print("\033[91m                              ______________                               ")
print("\033[91m                        ,===:'.,            `-._                           ")
print("\033[91m                             `:.`---.__         `-._                       ")
print("\033[91m                               `:.     `--.         `.                     ")
print("\033[91m                                 \.        `.         `.                   ")
print("\033[91m                         (,,(,    \.         `.   ____,-`.,                ")
print("\033[91m                      (,'     `/   \.   ,--.___`.'                         ")
print("\033[91m                  ,  ,'  ,--.  `,   \.;'         `                         ")
print("\033[91m                   `{D, {    \  :    \;                                    ")
print("\033[91m                     V,,'    /  /    //                                    ")
print("\033[91m                     j;;    /  ,' ,-//.    ,---.      ,                    ")
print("\033[91m                     \;'   /  ,' /  _  \  /  _  \   ,'/                    ")
print("\033[91m                           \   `'  / \  `'  / \  `.' /                     ")
print("\033[91m                           `.___,'   `.__,'   `.__,'  ")

print("")
time.sleep(.9)

print(chr(27)+'[2j')
print('\033c')
print('\x1bc')
print("\033[91m")

for x in range(9000):

 res = input("\033[91m"+curso+"\033[97m ")
 if res == "clear":
  print(chr(27)+'[2j')
  print('\033c')
  print('\x1bc')
 if res == "explorer":
  
  print("\033[91m[+]\033[97m Starting...")
  
  time.sleep(.5)
  print(chr(27)+'[2j')
  print('\033c')
  print('\x1bc')
  print("\033[92m#\033[97m Use CTRL+C to exit")
  os.system("python3 explorer.py")
 if res == "reboot":
  print(chr(27)+'[2j')
  print('\033c')
  print('\x1bc')
  print("\033[91m[+]\033[97m Rebooting...")
  time.sleep(.2)
  os.system("python3 lizard.py")
 if res == "sys":
  

  print('\033[97m Created By MarkynDev')
  print('\033[97m LizardOS Baseado em Python 3.7')
  print('\033[91m 1.2 \033[97m | \033[92mOPEN-BETA')

 if res == "echo":
  res = input("\033[97m ")

 if res == "ping":
  pop1 = input("\033[97mIP\033[92m> \033[97m")
  print('\033[92m#  \033[97mUse CTRL+C to stop! ')

  os.system("ping " + str(pop1) + " -c 5")
 if res == "run":
  print('\033[92m#  \033[97mUse this command to run python3 script or lizardmodules ')
  pop1 = input("\033[97mScript\033[92m> \033[97m")
  print('\033[92m#  \033[97mUse CTRL+C to stop! ')

  os.system("python3 " + str(pop1))
  
 if res == "dir":
	 
  os.system("dir")
 if res == "admin":
  pop1 = input("@Local\033[91m> \033[97m")
  os.system(pop1)
 if res == "date":
  os.system("date")
 if res == "netconfig":
  os.system("ifconfig")
 if res == "set":
  print("----------------------\033[92mMEMORYS\033[97m---------------------")
  print("|                                                |")
  print('|        memo1, memo2, memo3, cursor(STRING)     |')
  print("|                                                |")
  print("--------------------------------------------------")

  escl = input('\033[97mMemory\033[92m>  	\033[97m')
  if escl == "memo1":   
   print('\033[97m[Memory One]\033[97m \033[91m 2,5 Kb \033[97m/\033[92m 10 Kb')
   memo1 = input('\033[97mSet\033[92m>  	\033[97m') 
  if escl == "memo2":   
   print('\033[97m[Memory Two]\033[97m \033[91m 2,9 Kb \033[97m/\033[92m 10 Kb')
   memo2 = input('\033[97mSet\033[92m>  	\033[97m') 
  if escl == "memo3":   
   print('\033[97m[Memory Three]\033[97m \033[91m 3,1 Kb \033[97m/\033[92m 10 Kb')
   memo3 = input('\033[97mSet\033[92m>  	\033[97m') 
  if escl == "cursor":   
   print('\033[97m[ATUAL: '+curso+' ]\033[97m')
   curso = input('') 
 if res == "view":
  print("----------------------\033[92mMEMORYS\033[97m---------------------")
  print("|                                                |")
  print('|        memo1, memo2, memo3, cursor(STRING)     |')
  print("|                                                |")
  print("--------------------------------------------------")
  escl = input('\033[97mView\033[92m>  	\033[97m')
  if escl == "memo1":   
   print(memo1)
  if escl == "memo2":   
   print(memo2)
  if escl == "memo3":   
   print(memo3)
  	 
  
  


 if res == "get":
  url = input('\033[97m Download-URL: \033[97m')
  fileName = input('\033[97m FileName: \033[97m')
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

