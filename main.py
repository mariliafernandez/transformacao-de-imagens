import argparse
import cv2 as cv
import sys

# Inverte os valores de intensidade da imagem
def invert(img):
    for row in img:
        for pixel in row:
            intensisy = pixel[0]
            pixel[:] = 255 - intensisy
    cv.imshow('Inverted', img)
    cv.waitKey(0)
    cv.imwrite('inverted.jpg', img)

def switch_columns(img):
    print(2)

def switch_rows(img):
    print(3)

def histogram_stretching(img):
    print(4)
    
# Lê os argumentos passados via terminal
parser = argparse.ArgumentParser()
parser.add_argument('-t', help='operation', type=int)
parser.add_argument('-i', help='image')
args = parser.parse_args()
operation = args.t
image = args.i

# Abre a imagem em escala de cinza
img = cv.imread(image)
if img is None : sys.exit('Could not read the image.')
else: gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

if operation == 1: invert(gray)
elif operation == 2: switch_columns(gray)
elif operation == 3: switch_rows(gray)
elif operation == 4: histogram_stretching(gray)
else: print('Invalid option')