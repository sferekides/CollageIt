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
    img = cv.resize(image, (0,0), fx=0.50, fy=0.50)
    ReS_images.append(img)


# ****** Starting program with user input below ****** #

welcome = "Welcome to CollageIt!\nPlease input the word or words that you would like to display with images!\n"
print(welcome)

while True:
	outputMessage = input("What word or words would you like to display?\nPlease use all capital letters\n")
	if not outputMessage.isupper():
		print("Sorry, please use all capital letters only.\n")
		continue
	else:
		break

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

sortedVector = []

for index, image in zip(range(midPoint), Z) :
    blurred = cv.GaussianBlur(image, (11,11), 0) 
    sortedVector.append(blurred)

midPoint += 1
for image in Z[midPoint:]:
    brightened = cv.addWeighted(image, 2.5, numpy.zeros(image.shape, image.dtype), 0, 0)
    sortedVector.append(brightened)



col_1 = np.vstack([sortedVector[0],sortedVector[0],sortedVector[0]]) # Simply put the images in the list
col_2 = np.vstack([sortedVector[1],sortedVector[1],sortedVector[1]]) # Simply put the images in the list
col_3 = np.vstack([sortedVector[8],sortedVector[8],sortedVector[8]]) # Simply put the images in the list

collage = np.hstack([col_1, col_2,col_3])

cv.imshow('Image to display',collage)
cv.waitKey(0)

