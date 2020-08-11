# Marília Machado Fernandez
# RA: 1611739

import argparse
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


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
# Similar a função switch_columns, porém invertendo os índex de linha e coluna
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
    

# Plota o histograma (distribuição de instensidade) da imagem original e depois do stretching
def plot_histogram(original, stretched):
    # Cria uma figura dividida em duas partes com eixos compartilhados
    fig, axs = plt.subplots( 2, sharex=True, sharey=True )
    fig.suptitle('Histograma')

    # Cria um dicionário das frequências de intensidade da imagem original
    max1 = np.max(original)
    min1 = np.min(original)
    f1 = {}
    for i in range( min1, max1):
        f1[i] = np.sum( original == i )
    axis1 = f1.items()     
    x1, y1 = zip( *axis1 )

    # Cria um dicionário das frequências de intensidade da imagem após o histogram stretching
    max2 = np.max(stretched)
    min2 = np.min(stretched)
    f2 = {}
    for i in range( min2, max2):
        f2[i] = np.sum( stretched == i )
    axis2 = f2.items()  
    x2, y2 = zip( *axis2 )
    
    # Plota as duas frequênciasem gráfico de barras
    axs[0].bar( x1,y1 ) 
    axs[0].set_title('Original')

    axs[1].bar( x2,y2 )
    axs[1].set_title('Stretched')

    plt.show()


# Interpreta os argumentos passados via terminal
parser = argparse.ArgumentParser()
parser.add_argument('-t', help='operation [1, 2, 3, 4]', type=int)
parser.add_argument('-i', help='image in png format')
args = parser.parse_args()
operation = args.t
image = args.i

# Abre a imagem em escala de cinza
img_file = cv.imread(image)
if img_file is None : print('Não foi possível ler a imagem.')
else: 
    # Converte as cores originais da imagem para tons de cinza e salva a nova imagem em arquivo
    gray = cv.cvtColor(img_file, cv.COLOR_BGR2GRAY)
    cv.imwrite('input_tons_de_cinza.png', gray)

    # Escolhe a opção de transformação
    if operation == 1: 
        result = invert(gray)
    elif operation == 2: 
        result = switch_columns(gray)
    elif operation == 3: 
        result = switch_rows(gray)
    elif operation == 4: 
        result = histogram_stretching(gray)
        plot_histogram(gray, result)
    else: print('Invalid option')

    # Mostra o resultado e escreve em arquivo
    cv.imshow('Transformação', result)
    cv.waitKey(0)
    cv.imwrite('output.png', result)