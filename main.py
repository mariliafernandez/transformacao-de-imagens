# Marília Machado Fernandez
# RA: 1611739

import argparse
import cv2 as cv
import numpy as np

# Inverte os valores de intensidade da imagem
def invert(img):
    return 255-img
    
# Troca os valores de intensidade da imagem nas colunas pares com os valores nas colunas ímpares
def switch_columns(img):
    # Seleciona as colunas pares e ímpares e atribui a even e odd, respectivamente 
    even = img[:,::2] 
    odd = img[:,1::2] 

    # Reatribui aos valores das colunas pares os valores das colunas ímpares, e vice-versa
    img[:,::2] = odd 
    img[:,1::2] = even
    return img

# Troca os valores de intensidade da imagem nas linhas pares com os valores nas linhas ímpares
# Similar a função switch_columns, porém invertendo o índex de linha e coluna
def switch_rows(img):
    even = img[::2,:]
    odd = img[1::2,:]
    img[::2,:] = odd
    img[1::2,:] = even
    return img

# Alarga a faixa de contraste da imagem
def histogram_stretching(img):
    max_int = np.max(img)
    min_int = np.min(img)
    return int(255/(max_int-min_int))*(img-min_int)
    
# Interpreta os argumentos passados via terminal
parser = argparse.ArgumentParser()
parser.add_argument('-t', help='operation', type=int)
parser.add_argument('-i', help='image')
args = parser.parse_args()
operation = args.t
image = args.i

# Abre a imagem em escala de cinza
img_file = cv.imread(image)
if img_file is None : print('Não foi possível ler a imagem.')
else: 
    # Converte as cores originais da imagem para tons de cinza e salva a nova imagem em arquivo
    gray = cv.cvtColor(img_file, cv.COLOR_BGR2GRAY)
    cv.imshow('Tons de cinza', gray)
    cv.waitKey(0)
    cv.imwrite('cinza.jpg', gray)

    # Escolhe a opção de transformação
    if operation == 1: 
        result = invert(gray)
    elif operation == 2: 
        result = switch_columns(gray)
    elif operation == 3: 
        result = switch_rows(gray)
    elif operation == 4: 
        result = histogram_stretching(gray)
    else: print('Invalid option')

    # Mostra o resultado e escreve em arquivo
    cv.imshow('Transformação', result)
    cv.waitKey(0)
    cv.imwrite('output.jpg', result)