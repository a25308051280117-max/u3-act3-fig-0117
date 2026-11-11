import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2

#Matias Lope NC 0117
print("Matias Lopez NC 0117")
print("UIII Act3 colocar puntos a una imagen en blanco y negro")
img_josejose=cv2.imread('josejose.jpg')
plt.imshow(img_josejose)
plt.title('josejose y Matias Lopez NC 0117')
plt.show()
print("-+-+-++-+-+-+-+-puntos en la imagen-+-++-+++-+-+-+-+-+-+-+-+-+")
plt.imshow(img_josejose)
x=[100,100,500,500]
y=[100,400,500,300]
plt.scatter(x,y,s=20,c='red')
plt.show()
print("-+--+-+-cuadro azul en la imagen-+-+-+-++-")
img_josejose=cv2.imread('josejose.jpg')
plt.imshow(img_josejose)
#x=[200,100,500,100]
#y=[200,100,500,500]
x=[134,269,275,98]
y=[269,74,274,97]
plt.plot(x,y,c='blue')
plt.show()
print("-+-+-+circulo verde en la imagen-+-+-+-+-")
I=cv2.imread('josejose.jpg')




