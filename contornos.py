import cv2
import numpy as np


imagen = cv2.imread('dani1.jpg')
gray = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
,th =cv2.threshold(gray, 100,255, cv2.THRESH_BINARY)
img,contornos, hierarchy=cv2.findContours(th, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(imagen, contornos, -1, (0,255,0), 3)




cv2.imshow('th', th)
cv2.imshow('imagen', imagen)
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

