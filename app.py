import numpy as np
from PIL import ImageGrab
import cv2
import pyautogui

while(True):
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

                
        template = cv2.imread('1.png',0)
        w, h = template.shape[::-1]
        res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
        threshold = 0.8
        loc = np.where( res >= threshold)
        for pt in zip(*loc[::-1]):
                ww = int(w/2)
                hh = int(h/2)
                cv2.circle(img_rgb, (pt[0] + ww, pt[1] + hh), 3, (0,255,0))

        #Hueco
        template = cv2.imread('4.png',0)
        w, h = template.shape[::-1]
        res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
        threshold = 0.8
        loc = np.where( res >= threshold)
        for pt in zip(*loc[::-1]):
                ww = int(w/2)
                hh = int(h/2)
                cv2.circle(img_rgb, (pt[0] + ww, pt[1] + hh), 3, (0,255,0))
        cv2.resizeWindow('image', 460,780)
        cv2.moveWindow('image', 960, 200)
        cv2.imshow('image', img_rgb)
        cv2.waitKey(1)

        
