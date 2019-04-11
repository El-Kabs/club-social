import cv2
import numpy as np
from matplotlib import pyplot as plt
import numpy as np
from PIL import ImageGrab
import time
import pyautogui
import math

col=2
pos = (955, 790)

carrilUnoPos = (800,915)
carrilDosPos = (916,1000)
carrilTresPos = (1001,1100)

carrilUno = []
carrilDos = []
carrilTres = []

def moverCarril(carril):
	global pos
	global col
	while True:
		#print('COLUMNA ACTUAL',col)
		#print('CARRIL MOVER',carril)
		#print('------------------------')
		if col>carril:
			col-=1
			moverDerecha()
		if col<carril:
			col+=1
			moverIzquierda()
		if col==carril:
			break
			
	
	
def moverIzquierda():
	global pos
	global col
	pyautogui.press('left')
	pos = (pos[0]-80, 790)

def moverDerecha():
	global pos
	global col
	pyautogui.press('right')
	pos = (pos[0]+80, 790)

def darCarrilMasVacio():
	global carrilUno
	global carrilDos
	global carrilTres
	#print('Carril Uno ', carrilUno)
	#print('Carril Dos ', carrilDos)
	#print('Carril Uno ', carrilTres)
	if((len(carrilDos)==0)):
		return 2
	elif((len(carrilUno)==0)):
		return 1
	elif((len(carrilTres)==0)):
		return 3
	
	minimo = min(carrilUno[0][1], min(carrilDos[0][1], carrilTres[0][1]))
	if(minimo==carrilUno[0][1]):
		return 1
	elif(minimo==carrilDos[0][1]):
		return 2
	elif(minimo==carrilTres[0][1]):
		return 3	
		
time.sleep(3)
i = 0
while(True):
	#print('Iteracion ', i)
	carrilUno = []
	carrilDos = []
	carrilTres = []
	image = pyautogui.screenshot(region=(320,150,780,905))
	img_rgb = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
	img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
	
	
	
	#Enemigos
	template = cv2.imread('2.png',0)
	w, h = template.shape[::-1]

	res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
	threshold = 0.8
	loc = np.where( res >= threshold)
	for pt in zip(*loc[::-1]):
		ww = int(w/2)
		hh = int(h/2)
		cv2.circle(img_rgb, (pt[0] + ww, pt[1] + hh), 3, (0,255,0))
		centPos = (pt[0] + ww, pt[1] + hh)
		if(carrilUnoPos[0]<=centPos[0]<=carrilUnoPos[1]):
			carrilUno.append(centPos)
		elif(carrilDosPos[0]<=centPos[0]<=carrilDosPos[1]):
			carrilDos.append(centPos)
		elif(carrilTresPos[0]<=centPos[0]<=carrilTresPos[1]):
			carrilTres.append(centPos)
		
	template = cv2.imread('1.png',0)
	w, h = template.shape[::-1]

	res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
	threshold = 0.8
	loc = np.where( res >= threshold)
	for pt in zip(*loc[::-1]):
		ww = int(w/2)
		hh = int(h/2)
		cv2.circle(img_rgb, (pt[0] + ww, pt[1] + hh), 3, (0,255,0))
		centPos = (pt[0] + ww, pt[1] + hh)
		if(carrilUnoPos[0]<=centPos[0]<=carrilUnoPos[1]):
			carrilUno.append(centPos)
		elif(carrilDosPos[0]<=centPos[0]<=carrilDosPos[1]):
			carrilDos.append(centPos)
		elif(carrilTresPos[0]<=centPos[0]<=carrilTresPos[1]):
			carrilTres.append(centPos)
	
	#Hueco
	template = cv2.imread('4.png',0)
	w, h = template.shape[::-1]

	res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
	threshold = 0.8
	loc = np.where( res >= threshold)
	for pt in zip(*loc[::-1]):
		ww = int(w/2)
		hh = int(h/2)
		cv2.circle(img_rgb, (pt[0] + ww, pt[1] + hh), 3, (0,0,255))
		centPos = (pt[0] + ww, pt[1] + hh)
		if(carrilUnoPos[0]<=centPos[0]<=carrilUnoPos[1]):
			carrilUno.append(centPos)
		elif(carrilDosPos[0]<=centPos[0]<=carrilDosPos[1]):
			carrilDos.append(centPos)
		elif(carrilTresPos[0]<=centPos[0]<=carrilTresPos[1]):
			carrilTres.append(centPos)
			
	#Player
	template = cv2.imread('3.png',0)
	w, h = template.shape[::-1]

	res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
	threshold = 0.8
	loc = np.where( res >= threshold)
	for pt in zip(*loc[::-1]):
		ww = int(w/2)
		hh = int(h/2)
		cv2.circle(img_rgb, (pt[0] + ww, pt[1] + hh), 3, (255,0,0))
	

	
	cv2.resizeWindow('image', 460,780)
	cv2.moveWindow('image', 960, 250)
	cv2.imshow('image', img_rgb)
	cv2.waitKey(1)
	i = i + 1
	
	carrilUno = sorted(carrilUno, key=lambda x: x[1])
	carrilDos = sorted(carrilDos, key=lambda x: x[1])
	carrilTres = sorted(carrilTres, key=lambda x: x[1])
	
	#Analisis
	moverCarril(darCarrilMasVacio())
	
