# pip install opencv-python (executar no cmd/prompt de comando)
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('numeros.png',cv2.IMREAD_GRAYSCALE)
'''
print(img.shape)
print(img.size)
print(img.dtype)

cv2.imshow('image',img)
cv2.waitKey(5000)
cv2.destroyAllWindows()

px = img[48,214]
print(px)
'''
histograma = [0] * 256
# monta o histograma percorrendo as linhas e colunas e somando 1 na posição do array equivalente a cor
linha  = img.shape[0] - 1
coluna = img.shape[1] - 1
'''
for i in range(0,linha):
    for j in range(0,coluna):
        histograma[img[i,j]] = histograma[img[i,j]] + 1

print("Histograma da imagem original em cinza")
print(histograma)
'''
def find_upper_line( limite ):
    for i in range(0,linha):
        for j in range(0,coluna):
            if img[i,j] < limite:
                return i

def find_upper_column( limite ):
    for i in range(0,coluna):
        for j in range(0,linha):
            if img[j,i] < limite:
                return i

def find_lower_line( limite ):
    for i in range(linha,-1,-1):
        for j in range(coluna,-1,-1):
            if img[i,j] < limite:
                return i

def find_lower_column( limite ):
    for i in range(coluna,-1,-1):
        for j in range(linha,-1,-1):
            if img[j,i] < limite:
                return i

threshold=240
upper_bound=[0,0]
lower_bound=[linha - 1,coluna - 1]
upper_bound[0] = find_upper_line(threshold)
upper_bound[1] = find_upper_column(threshold)
lower_bound[0] = find_lower_line(threshold)
lower_bound[1] = find_lower_column(threshold)

imgnew = img[upper_bound[0]:lower_bound[0],upper_bound[1]:lower_bound[1]]
'''
print(imgnew.shape)
print(imgnew.size)
print(imgnew.dtype)
cv2.imshow('image',imgnew)
cv2.waitKey(5000)
cv2.destroyAllWindows()
'''
linha  = imgnew.shape[0] - 1
coluna = imgnew.shape[1] - 1
'''
for i in range(0,linha):
    for j in range(0,coluna):
        histograma[imgnew[i,j]] = histograma[imgnew[i,j]] + 1
print("Histograma da imagem original em cinza")
print(histograma)
'''
imgone = imgnew[0:51,0:37]
imgtwo = imgnew[0:51,37:75]
imgthree = imgnew[0:51,75:115]
imgfour = imgnew[0:51,105:160]
imgfive = imgnew[0:51,0:38]
imgsix = imgnew[0:51,0:38]
imgseven = imgnew[0:51,0:38]
imgeight = imgnew[51:102,80:115]
imgnine = imgnew[51:102,0:38]

cv2.imshow('image',imgone) # Mostra a imagem
cv2.waitKey(3000)
cv2.destroyAllWindows()

linha  = imgone.shape[0] - 1
coluna = imgone.shape[1] - 1
for i in range(0,linha):
    for j in range(0,coluna):
        histograma[imgnew[i,j]] = histograma[imgnew[i,j]] + 1
print("Histograma da imagem 1 em cinza")
print(histograma)
linha  = imgeight.shape[0] - 1
coluna = imgeight.shape[1] - 1
for i in range(0,linha):
    for j in range(0,coluna):
        histograma[imgnew[i,j]] = histograma[imgnew[i,j]] + 1
print("Histograma da imagem 8 em cinza")
print(histograma)