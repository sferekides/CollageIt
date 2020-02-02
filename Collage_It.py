import cv2 as cv
import numpy as np
import os
import random

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

    cols = np.hstack([col_1, col_2,col_3, col_4,col_5])
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

    cols = np.hstack([col_1, col_2,col_3, col_4,col_5])
    return cols

def letterC(textImages, backgroundImages):
    b = len(backgroundImages)
    t = len(textImages)

    col_1 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)],textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_2 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)],backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(a)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_3 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)],backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(a)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_4 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)],backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(a)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_5 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)],backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(a)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 

    cols = np.hstack([col_1, col_2,col_3, col_4,col_5])
    return cols

def letterD(textImages, backgroundImages):
    b = len(backgroundImages)
    t = len(textImages)

    col_1 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)],textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_2 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)],backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_3 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)],backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_4 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)],backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_5 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)],textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)]])

    cols = np.hstack([col_1, col_2,col_3, col_4,col_5])
    return cols

def letterE(textImages, backgroundImages):
    b = len(backgroundImages)
    t = len(textImages)

    col_1 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)],textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_2 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)],backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_3 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)],backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_4 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)],backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_5 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)],backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 

    cols = np.hstack([col_1, col_2,col_3, col_4,col_5])
    return cols

def letterF(textImages, backgroundImages):
    b = len(backgroundImages)
    t = len(textImages)

    col_1 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_2 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_3 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_4 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_5 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 

    cols = np.hstack([col_1, col_2,col_3, col_4,col_5])
    return cols

def letterG(textImages, backgroundImages):
    b = len(backgroundImages)
    t = len(textImages)

    col_1 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_2 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_3 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)],backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_4 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)],backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_5 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)],backgroundImages[rand(b)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 

    cols = np.hstack([col_1, col_2,col_3, col_4,col_5])
    return cols

def letterH(textImages, backgroundImages):
    b = len(backgroundImages)
    t = len(textImages)

    col_1 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_2 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_3 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_4 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_5 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 

    cols = np.hstack([col_1, col_2,col_3, col_4,col_5])
    return cols

def letterI(textImages, backgroundImages):
    b = len(backgroundImages)
    t = len(textImages)
    col_1 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_2 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_3 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_4 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_5 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    cols = np.hstack([col_1, col_2,col_3, col_4,col_5])
    return cols

def letterJ(textImages, backgroundImages):
    b = len(backgroundImages)
    t = len(textImages)
    col_1 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_2 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_3 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_4 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_5 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    cols = np.hstack([col_1, col_2,col_3, col_4,col_5])
    return cols

def letterK(textImages, backgroundImages):
    b = len(backgroundImages)
    t = len(textImages)
    col_1 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]])
    col_2 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)]])  
    col_3 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)]])  
    col_4 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_5 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    cols = np.hstack([col_1, col_2,col_3, col_4,col_5])
    return cols

def letterL(textImages, backgroundImages):
    b = len(backgroundImages)
    t = len(textImages)
    col_1 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_2 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_3 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_4 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_5 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    cols = np.hstack([col_1, col_2,col_3, col_4,col_5])
    return cols

def letterM(textImages, backgroundImages):
    b = len(backgroundImages)
    t = len(textImages)
    col_1 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_2 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_3 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)]])  
    col_4 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_5 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    cols = np.hstack([col_1, col_2,col_3, col_4,col_5])
    return cols

def letterN(textImages, backgroundImages):
    b = len(backgroundImages)
    t = len(textImages)
    col_1 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_2 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_3 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)]])  
    col_4 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_5 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    cols = np.hstack([col_1, col_2,col_3, col_4,col_5])
    return cols

def letterO(textImages, backgroundImages):
    b = len(backgroundImages)
    t = len(textImages)
    col_1 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_2 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_3 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_4 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_5 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    cols = np.hstack([col_1, col_2,col_3, col_4,col_5])
    return cols

def letterP(textImages, backgroundImages):
    b = len(backgroundImages)
    t = len(textImages)
    col_1 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_2 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_3 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_4 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_5 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    cols = np.hstack([col_1, col_2,col_3, col_4,col_5])
    return cols

def letterQ(textImages, backgroundImages):
    b = len(backgroundImages)
    t = len(textImages)
    col_1 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_2 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_3 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_4 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_5 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    cols = np.hstack([col_1, col_2,col_3, col_4,col_5])
    return cols

def letterR(textImages, backgroundImages):
    b = len(backgroundImages)
    t = len(textImages)
    col_1 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_2 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_3 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_4 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], textImages[rand(t)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_5 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    cols = np.hstack([col_1, col_2,col_3, col_4,col_5])
    return cols

def letterS(textImages, backgroundImages):
    b = len(backgroundImages)
    t = len(textImages)
    col_1 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_2 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_3 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_4 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_5 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    cols = np.hstack([col_1, col_2,col_3, col_4,col_5])
    return cols

def letterT(textImages, backgroundImages):
    b = len(backgroundImages)
    t = len(textImages)
    col_1 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_2 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_3 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_4 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_5 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    cols = np.hstack([col_1, col_2,col_3, col_4,col_5])
    return cols

def letterU(textImages, backgroundImages):
    b = len(backgroundImages)
    t = len(textImages)
    col_1 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_2 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_3 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_4 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_5 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    cols = np.hstack([col_1, col_2,col_3, col_4,col_5])
    return cols

def letterV(textImages, backgroundImages):
    b = len(backgroundImages)
    t = len(textImages)
    col_1 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_2 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_3 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_4 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_5 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    cols = np.hstack([col_1, col_2,col_3, col_4,col_5])
    return cols

def letterW(textImages, backgroundImages):
    b = len(backgroundImages)
    t = len(textImages)
    col_1 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_2 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_3 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_4 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_5 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    cols = np.hstack([col_1, col_2,col_3, col_4,col_5])
    return cols

def letterX(textImages, backgroundImages):
    b = len(backgroundImages)
    t = len(textImages)
    col_1 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_2 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_3 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)]])  
    col_4 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_5 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    cols = np.hstack([col_1, col_2,col_3, col_4,col_5])
    return cols

def letterY(textImages, backgroundImages):
    b = len(backgroundImages)
    t = len(textImages)
    col_1 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_2 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_3 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], textImages[rand(t)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]])  
    col_4 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_5 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    cols = np.hstack([col_1, col_2,col_3, col_4,col_5])
    return cols

def letterZ(textImages, backgroundImages):
    b = len(backgroundImages)
    t = len(textImages)
    col_1 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_2 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_3 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]])  
    col_4 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    col_5 = np.vstack([backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)], backgroundImages[rand(b)], textImages[rand(t)], backgroundImages[rand(b)], backgroundImages[rand(b)]]) 
    cols = np.hstack([col_1, col_2,col_3, col_4,col_5])
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
    img = cv.resize(image, (0,0), fx=0.25, fy=0.25)
    ReS_images.append(img)

#white image
white_img = np.zeros([100, 100, 3], dtype=np.uint8)
white_img.fill(255)
whiteImages = [white_img]

#black image
black_img = np.zeros([100, 100, 3], dtype=np.uint8)
black_img.fill(0)
blackImages = [black_img]

# ****** Starting program with user input below ****** #

welcome = "Welcome to CollageIt!\nPlease input the word or words that you would like to display with images!\n"
print(welcome)

outputMessage = input("What word or words would you like to display?\n")

#this method will tell you what the width of the collage must be.
width_of_collage = determine_length_of_image(outputMessage)
print(width_of_collage)

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
#print(ranking)

midPoint = int((len(Z) / 2))

darkImages = []
lightImages = []

for index, image in zip(range(midPoint), Z) :
    blurred = cv.GaussianBlur(image, (3,3), 0) 
    darkImages.append(blurred)

midPoint += 1
for image in Z[midPoint:]:
    brightened = cv.addWeighted(image, 1.1, np.zeros(image.shape, image.dtype), 0, 0)
    lightImages.append(brightened)


col_1 = np.vstack([darkImages[0],darkImages[1], darkImages[2]]) # Simply put the images in the list
col_2 = np.vstack([darkImages[2],darkImages[3], darkImages[4]]) # Simply put the images in the list
col_3 = np.vstack([lightImages[0],lightImages[1], lightImages[2]]) # Simply put the images in the list
col_4 = np.vstack([lightImages[2],lightImages[3], lightImages[3]]) # Simply put the images in the list


collage = np.hstack([col_1, col_2, col_3, col_4])

#cv.imshow('Image to display',collage)
#cv.waitKey(0)

cv.imshow('Image to display',collage)
cv.waitKey(0)

