import cv2 as cv
import numpy as np
import os

#function that I found on Stack Overflow and modified to fit our needs 
#pass in folder name to method and will iterate through folder and load all images using openCV function call
def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv.imread(os.path.join(folder,filename))
        if img is not None:
            images.append(img)
    return images

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


# ****** Starting program with user input below ****** #

welcome = "Welcome to CollageIt!\nPlease input the word or words that you would like to display with images!\n"
print(welcome)

outputMessage = input("What word or words would you like to display?\n")

col_1 = np.vstack([ReS_images[0],ReS_images[1], ReS_images[2]]) # Simply put the images in the list
col_2 = np.vstack([ReS_images[0],ReS_images[1], ReS_images[2]]) # Simply put the images in the list
col_3 = np.vstack([ReS_images[0],ReS_images[1], ReS_images[2]]) # Simply put the images in the list
col_4 = np.vstack([ReS_images[0],ReS_images[1], ReS_images[2]]) # Simply put the images in the list
col_5 = np.vstack([ReS_images[0],ReS_images[1], ReS_images[2]]) # Simply put the images in the list
col_6 = np.vstack([ReS_images[0],ReS_images[1], ReS_images[2]]) # Simply put the images in the list
col_7 = np.vstack([ReS_images[0],ReS_images[1], ReS_images[2]]) # Simply put the images in the list
col_8 = np.vstack([ReS_images[0],ReS_images[1], ReS_images[2]]) # Simply put the images in the list
col_9 = np.vstack([ReS_images[0],ReS_images[1], ReS_images[2]]) # Simply put the images in the list
col_10 = np.vstack([ReS_images[0],ReS_images[1], ReS_images[2]]) # Simply put the images in the list
col_11 = np.vstack([ReS_images[0],ReS_images[1], ReS_images[2]]) # Simply put the images in the list
col_12 = np.vstack([ReS_images[0],ReS_images[1], ReS_images[2]]) # Simply put the images in the list
col_13 = np.vstack([ReS_images[0],ReS_images[1], ReS_images[2]]) # Simply put the images in the list
col_14 = np.vstack([ReS_images[0],ReS_images[1], ReS_images[2]]) # Simply put the images in the list

collage = np.hstack([col_1, col_2,col_3, col_4,col_5, col_6,col_7, col_8,col_9, col_10,col_11, col_12,col_13, col_14])

cv.imshow('Image to display',collage)
cv.waitKey(0)