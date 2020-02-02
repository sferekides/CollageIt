import cv2 as cv
import numpy as np
import os
import random
from datetime import datetime

#function that I found on Stack Overflow and modified to fit our needs 
#pass in folder name to method and will iterate through folder and load all images using openCV function call
def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv.imread(os.path.join(folder,filename))
        if img is not None:
            images.append(img)
    return images


    #Modular Letter Art begins here
def letterA(textImages, backgroundImages):
    b = len(backgroundImages)
    t = len(textImages)

    col_1 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_2 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_3 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)]])  
    col_4 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_5 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 

    cols = np.hstack([col_1, col_2, col_3, col_4, col_5])
    return cols

#messed up go back and fix
def letterB(textImages, backgroundImages):
    b = len(backgroundImages)
    t = len(textImages)
    col_1 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_2 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]])  
    col_3 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_4 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_5 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)]])

    cols = np.hstack([col_1, col_2, col_3, col_4, col_5])
    return cols

def letterC(textImages, backgroundImages):
    b = len(backgroundImages)
    t = len(textImages)

    col_1 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)],textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_2 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)],backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(a)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_3 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)],backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(a)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_4 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)],backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(a)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_5 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)],backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(a)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 

    cols = np.hstack([col_1, col_2, col_3, col_4, col_5])
    return cols

def letterD(textImages, backgroundImages):
    b = len(backgroundImages)
    t = len(textImages)

    col_1 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)],textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_2 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)],backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_3 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)],backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_4 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)],backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_5 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)],textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)]])

    cols = np.hstack([col_1, col_2, col_3, col_4, col_5])
    return cols

def letterE(textImages, backgroundImages):
    b = len(backgroundImages)
    t = len(textImages)

    col_1 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)],textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_2 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)],backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_3 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)],backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_4 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)],backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_5 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)],backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 

    cols = np.hstack([col_1, col_2, col_3, col_4, col_5])
    return cols

def letterF(textImages, backgroundImages):
    b = len(backgroundImages)
    t = len(textImages)

    col_1 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_2 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_3 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_4 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_5 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 

    cols = np.hstack([col_1, col_2, col_3, col_4, col_5])
    return cols

def letterG(textImages, backgroundImages):
    b = len(backgroundImages)
    t = len(textImages)

    col_1 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_2 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_3 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)],backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_4 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)],backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_5 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)],backgroundImages[rand(b)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 

    cols = np.hstack([col_1, col_2, col_3, col_4, col_5])
    return cols

def letterH(textImages, backgroundImages):
    b = len(backgroundImages)
    t = len(textImages)

    col_1 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_2 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_3 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_4 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_5 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 

    cols = np.hstack([col_1, col_2, col_3, col_4, col_5])
    return cols

def letterI(textImages, backgroundImages):
    b = len(backgroundImages)
    t = len(textImages)
    col_1 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_2 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_3 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_4 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_5 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    cols = np.hstack([col_1, col_2, col_3, col_4, col_5])
    return cols

def letterJ(textImages, backgroundImages):
    b = len(backgroundImages)
    t = len(textImages)
    col_1 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_2 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_3 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_4 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_5 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    cols = np.hstack([col_1, col_2, col_3, col_4, col_5])
    return cols

def letterK(textImages, backgroundImages):
    b = len(backgroundImages)
    t = len(textImages)
    col_1 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]])
    col_2 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)]])  
    col_3 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)]])  
    col_4 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_5 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    cols = np.hstack([col_1, col_2, col_3, col_4, col_5])
    return cols

def letterL(textImages, backgroundImages):
    b = len(backgroundImages)
    t = len(textImages)
    col_1 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_2 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_3 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_4 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_5 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    cols = np.hstack([col_1, col_2, col_3, col_4, col_5])
    return cols

def letterM(textImages, backgroundImages):
    b = len(backgroundImages)
    t = len(textImages)
    col_1 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_2 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_3 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)]])  
    col_4 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_5 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    cols = np.hstack([col_1, col_2, col_3, col_4, col_5])
    return cols

def letterN(textImages, backgroundImages):
    b = len(backgroundImages)
    t = len(textImages)
    col_1 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_2 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_3 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)]])  
    col_4 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_5 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    cols = np.hstack([col_1, col_2, col_3, col_4, col_5])
    return cols

def letterO(textImages, backgroundImages):
    b = len(backgroundImages)
    t = len(textImages)
    col_1 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_2 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_3 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_4 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_5 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    cols = np.hstack([col_1, col_2, col_3, col_4, col_5])
    return cols

def letterP(textImages, backgroundImages):
    b = len(backgroundImages)
    t = len(textImages)
    col_1 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_2 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_3 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_4 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_5 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    cols = np.hstack([col_1, col_2, col_3, col_4, col_5])
    return cols

def letterQ(textImages, backgroundImages):
    b = len(backgroundImages)
    t = len(textImages)
    col_1 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_2 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_3 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_4 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_5 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    cols = np.hstack([col_1, col_2, col_3, col_4, col_5])
    return cols

def letterR(textImages, backgroundImages):
    b = len(backgroundImages)
    t = len(textImages)
    col_1 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_2 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_3 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_4 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], textImages[rand(t)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_5 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    cols = np.hstack([col_1, col_2, col_3, col_4, col_5])
    return cols

def letterS(textImages, backgroundImages):
    b = len(backgroundImages)
    t = len(textImages)
    col_1 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_2 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_3 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_4 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_5 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    cols = np.hstack([col_1, col_2, col_3, col_4, col_5])
    return cols

def letterT(textImages, backgroundImages):
    b = len(backgroundImages)
    t = len(textImages)
    col_1 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_2 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_3 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_4 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_5 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    cols = np.hstack([col_1, col_2, col_3, col_4, col_5])
    return cols

def letterU(textImages, backgroundImages):
    b = len(backgroundImages)
    t = len(textImages)
    col_1 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_2 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_3 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_4 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_5 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    cols = np.hstack([col_1, col_2, col_3, col_4, col_5])
    return cols

def letterV(textImages, backgroundImages):
    b = len(backgroundImages)
    t = len(textImages)
    col_1 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_2 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_3 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_4 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_5 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    cols = np.hstack([col_1, col_2, col_3, col_4, col_5])
    return cols

def letterW(textImages, backgroundImages):
    b = len(backgroundImages)
    t = len(textImages)
    col_1 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_2 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_3 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_4 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_5 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    cols = np.hstack([col_1, col_2, col_3, col_4, col_5])
    return cols

def letterX(textImages, backgroundImages):
    b = len(backgroundImages)
    t = len(textImages)
    col_1 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_2 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_3 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)]])  
    col_4 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_5 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    cols = np.hstack([col_1, col_2, col_3, col_4, col_5])
    return cols

def letterY(textImages, backgroundImages):
    b = len(backgroundImages)
    t = len(textImages)
    col_1 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_2 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_3 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]])  
    col_4 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_5 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    cols = np.hstack([col_1, col_2, col_3, col_4, col_5])
    return cols

def letterZ(textImages, backgroundImages):
    b = len(backgroundImages)
    t = len(textImages)
    col_1 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_2 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_3 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]])  
    col_4 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_5 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    cols = np.hstack([col_1, col_2, col_3, col_4, col_5])
    return cols

def letterSpace(textImages, backgroundImages) :
    b = len(backgroundImages)
    t = len(textImages)
    col =  np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    cols = np.hstack([col])
    return cols

def wordSpace(textImages, backgroundImages) :
    b = len(backgroundImages)
    t = len(textImages)
    col_1 =  np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)]])
    col_2 =  np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)]])
    col_3 =  np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)]])
    cols = np.hstack([col_1, col_2, col_3])
    return cols

def rand(size):
    return random.randint(0, size-1)

def determine_length_of_image(user_input):
    total = 9
    for charac in user_input :
        if charac==' ':
            total+=2
        else :
            total+=6
    return total
        
#calls method that will load images and place them in an array
stored_images = load_images_from_folder('Images_For_Hack')

#test to check if stored images are loading properly - can copy and paste to test other modifications to the images
#commented out so that I don't display images every time
#for image in ReS_images:
#    cv.imshow('Image to display',image)
#    cv.waitKey(0)

#used to determine length of the array
#print(len(ReS_images))
BG_images = []
#will apply grayscale and resize all the images
for image in stored_images:
    img = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    BG_images.append(img)

ReS_images = []

for image in BG_images:
    img = cv.resize(image, (0,0), fx=0.09, fy=0.09)
    height, width = img.shape[0:2]
    ReS_images.append(img)


#white image for testing
#white_img = np.zeros([100, 100, 3], dtype=np.uint8)
#white_img.fill(255)
#whiteImages = [white_img]

#black image for testing
black_img = np.zeros([100, 100, 3], dtype=np.uint8)
black_img.fill(5)
blackImages = [black_img]

# ****** Starting program with user input below ****** #

welcome = "Welcome to CollageIt!\nPlease input the word or words that you would like to display with images!\n"
print(welcome)

outputMessage = input("What word or words would you like to display?\n")

#this method will tell you what the width of the collage must be.
width_of_collage = determine_length_of_image(outputMessage)

sumGray = 0
ranking = []
for images in  ReS_images :
    for i in range (images.shape[0]): #from zero to height
        for j in range (images.shape[1]): #from zero to width 
           sumGray += images[i][j]
    numPixels = images.shape[0] * images.shape[0]          
    sumGray /= numPixels
    ranking.append(sumGray)
    sumGray = 0

Z = [x for _,x in sorted(zip(ranking,ReS_images))]

midPoint = int((len(Z) / 2))

darkImages = []
lightImages = []

gray_img = np.zeros([54, 54], dtype=np.uint8)
gray_img.fill(254)

darkened_Images = []

for index, image in zip(range(midPoint), Z) :
    darkened = cv.addWeighted(image, 0.4, gray_img, 0.1,0)
    darkened_Images.append(darkened)

for image in darkened_Images :
    blurred = cv.GaussianBlur(image, (1,1), 0) 
    darkImages.append(blurred)

midPoint += 1
for image in Z[midPoint:]:
    brightened = cv.addWeighted(image, 0.8, np.zeros(image.shape, image.dtype), 0, 0)
    lightImages.append(brightened)

random.seed(datetime.now())
def output_columns(user_input) :
    columns = []
    for x in range(3):
        vec = letterSpace(lightImages, darkImages)
        columns.append(vec)
    for charac in user_input :
        vec = []
        if charac=='a' or charac =='A':
            vec = letterA(lightImages, darkImages)
            columns.append(vec)
        if charac=='b' or charac =='B':
            vec = letterB(lightImages, darkImages)
            columns.append(vec)
        if charac=='c' or charac =='C':
            vec = letterC(lightImages, darkImages)
            columns.append(vec)
        if charac=='d' or charac =='D':
            vec = letterD(lightImages, darkImages)
            columns.append(vec)
        if charac=='e' or charac =='E':
            vec = letterE(lightImages, darkImages)
            columns.append(vec)
        if charac=='f' or charac =='F':
            vec = letterF(lightImages, darkImages)
            columns.append(vec)
        if charac=='g' or charac =='G':
            vec = letterG(lightImages, darkImages)
            columns.append(vec)
        if charac=='h' or charac =='H':
            vec = letterH(lightImages, darkImages)
            columns.append(vec)
        if charac=='i' or charac =='I':
            vec = letterI(lightImages, darkImages)
            columns.append(vec)
        if charac=='j' or charac =='J':
            vec = letterJ(lightImages, darkImages)
            columns.append(vec)
        if charac=='k' or charac =='K':
            vec = letterK(lightImages, darkImages)
            columns.append(vec)
        if charac=='l' or charac =='L':
            vec = letterL(lightImages, darkImages)
            columns.append(vec)
        if charac=='m' or charac =='M':
            vec = letterM(lightImages, darkImages)
            columns.append(vec)
        if charac=='n' or charac =='N':
            vec = letterN(lightImages, darkImages)
            columns.append(vec)
        if charac=='o' or charac =='O':
            vec = letterO(lightImages, darkImages)
            columns.append(vec)
        if charac=='p' or charac =='P':
            vec = letterP(lightImages, darkImages)
            columns.append(vec)
        if charac=='q' or charac =='Q':
            vec = letterQ(lightImages, darkImages)
            columns.append(vec)
        if charac=='r' or charac =='R':
            vec = letterR(lightImages, darkImages)
            columns.append(vec)
        if charac=='s' or charac =='S':
            vec = letterS(lightImages, darkImages)
            columns.append(vec)
        if charac=='t' or charac =='T':
            vec = letterT(lightImages, darkImages)
            columns.append(vec)
        if charac=='u' or charac =='U':
            vec = letterU(lightImages, darkImages)
            columns.append(vec)
        if charac=='v' or charac =='V':
            vec = letterV(lightImages, darkImages)
            columns.append(vec)
        if charac=='w' or charac =='W':
            vec = letterW(lightImages, darkImages)
            columns.append(vec)
        if charac=='x' or charac =='X':
            vec = letterX(lightImages, darkImages)
            columns.append(vec)
        if charac=='y' or charac =='Y':
            vec = letterY(lightImages, darkImages)
            columns.append(vec)
        if charac=='z' or charac =='Z':
            vec = letterZ(lightImages, darkImages)
            columns.append(vec)
        vec = letterSpace(lightImages, darkImages)
        columns.append(vec)
    
    for x in range(2):
        vec = letterSpace(lightImages, darkImages)
        columns.append(vec)  
    return columns


fullImage = output_columns(outputMessage)

collage = np.hstack(fullImage)

collage = cv.resize(collage, (0,0), fx=0.5, fy=0.5)

cv.imshow('Image to display',collage)
cv.imwrite( "Gray_Image.jpg", collage )
#cv.waitKey(0)

