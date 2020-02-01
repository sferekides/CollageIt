import cv2 as cv
import numpy
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
#for image in stored_images:
#    cv.imshow('Image to display',image)
#    cv.waitKey(0)

#used to determine length of the array
#print(len(stored_images))



# ****** Starting program with user input below ****** #
welcome = "Welcome to CollageIt!\nPlease input the word or words that you would like to display with images!\n"
print(welcome)

outputMessage = input("What word or words would you like to display?\n")