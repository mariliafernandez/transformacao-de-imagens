# Marília Machado Fernandez
# RA: 1611739

import argparse
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from operation import *
import sys

# Interpreta os argumentos passados via terminal
parser = argparse.ArgumentParser()
parser.add_argument('-t', help='option [1, 2, 3, 4]', type=int)
parser.add_argument('-i', help='image in png format')
args = parser.parse_args()
option = args.t
image = args.i

# Abre a imagem em escala de cinza
img_file = cv.imread(image)
if img_file is None : 
    print('Não foi possível ler a imagem.')
    sys.exit(0)
else: 
    # Converte as cores originais da imagem para tons de cinza e salva a nova imagem em arquivo
    gray = cv.cvtColor(img_file, cv.COLOR_BGR2GRAY)
    cv.imwrite('input_tons_de_cinza.png', gray)

    # Escolhe a opção de transformação
    if option == 1: 
        result = invert(gray)
    elif option == 2: 
        result = switch_columns(gray)
    elif option == 3: 
        result = switch_rows(gray)
    elif option == 4: 
        result = histogram_stretching(gray)
        plot_histogram(gray, result)
    else: 
        print('Opção inválida.')
        sys.exit(0)

    # Mostra o resultado e escreve em arquivo
    cv.imshow('Transformação', result)
    cv.waitKey(0)
    cv.imwrite('output.png', result)