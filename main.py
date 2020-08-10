import argparse
import cv2 as cv
import sys

def invert(img):
    print(1)

def switch_columns(img):
    print(2)

def switch_rows(img):
    print(3)

def histogram_stretching(img):
    print(4)
    

parser = argparse.ArgumentParser()
parser.add_argument('-t', help='operation', type=int)
parser.add_argument('-i', help='image')

args = parser.parse_args()

operation = args.t
image = args.i

img = cv.imread(image)

if img is None:
    sys.exit('Could not read the image.')

if operation == 1: invert(img)
elif operation == 2: switch_columns(img)
elif operation == 3: switch_rows(img)
elif operation == 4: histogram_stretching(img)
else: print('Invalid option')