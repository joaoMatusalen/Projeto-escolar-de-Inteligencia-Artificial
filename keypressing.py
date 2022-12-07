import subprocess   
import time
import pyautogui
import serial
#subprocess.call([r'C:\Program Files\Mozilla Firefox\Firefox.exe',  # se voce quiser nao tiver o google chorme, coloque o local do seu navegador.
#    '-new-tab', 'https://chromedino.com/'])  # abrindo o navegador e o dino game.
          								     # se voce nao for um usuario de chorme, voce nao tera o Dino game. 
          								     # eu usei o site chromedino para abrir o game. 
time.sleep(6)                 #give a short time to open and setup all.
print("All sett :)")

ser = serial.Serial('COM4')		# atualize de acordo com a porta do seu arduino [port]
ser.baudrate = '9600'			#set baudRate

while True:						# looping. 
  h1=ser.readline() 			# lendo os dados do serial. 
  if h1:
   ss = int(h1.decode('utf-8')) # encode and make a int value
   if ss== 1:					# true while obstacle. 
   	print("Pulo !! ")		
   	pyautogui.press('up') 		#Auto press [UP] key           