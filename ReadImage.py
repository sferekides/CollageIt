import cv2 as cv
import numpy

# NOTE: ignore errors on cv - it will work regardless and I believe it is just a problem with the linter not identifying this edition

#will work with both .jpg and .png files
img_j = cv.imread("Picture2.jpg")
cv.imshow('FLEG Logo - Original', img_j)
#Note: problem with the imported file that it is not completely displaying

# type() method will get you the image type of whatever you have loaded
# General: use print() in Python to print out values (useful for debugging)
print(type(img_j))
#Note: if you look at the output then you will see that 

#following line assigns height and width to their respective values
height, width = img_j.shape[0:2]
print(img_j.shape)
print(height, width)
#following lines assign new dimensions for the photograpm scaled by a factor to their width and height
#note that values must be cast to int so that they are digit values (they are defining column/row lengths)
startRow = int(height*.15)
startCol = int(width*.15)
endRow = int(height*.85)
endCol = int(width*.85)
print(startCol,startRow,endCol,endRow)
#creates a new image file with cropped values retrieved from previous lines of code
croppedImage = img_j[startRow:endRow, startCol:endCol]
#Note that you can change the message on the top of the image window using the first parameter of the imshow function
cv.imshow('FLEG Logo - Cropped', croppedImage)
#setting the waitKey() to 0 allows the picture to be displayed infinitely and will not close until you x-out of the window
cv.waitKey(0)

#Following lines will display how to scale an image down - in this case to 75% of the original size
newImg = cv.resize(img_j, (0,0), fx=0.75, fy=0.75)
cv.imshow('FLEG logo - Resized', newImg)
cv.waitKey(0)

#This next technique is for adjusting the brightness of an image.
#I believe that we should use it for brightening light images that we will use to write or dark images if it were reversed
#My understanding of this method is that it takes a zeroes vector and somehow weights the image with them. I believe that you
# should be able to do the opposite with black but it might be more difficult to figure out how to do this
contrast_img = cv.addWeighted(img_j, 0.4, numpy.zeros(img_j.shape, img_j.dtype), 0, 0)
cv.imshow('FLEG logo - Brightened', contrast_img)
cv.waitKey(0)

#use the following function to blur photos
#key things here are that the (11,11) need to be odd and positive. Higher the number the higher the blur
#try changing to (111,111) to see the difference
blur_image = cv.GaussianBlur(img_j, (11,11), 0) 
cv.imshow('FLEG logo - Blurred', blur_image)
cv.waitKey(0)

#NOTE: here is the grayscale method!!! It is super straightforward and easy to understand
gray_img = cv.cvtColor(img_j, cv.COLOR_BGR2GRAY)
cv.imshow('FLEG logo - Gray-Scaled', gray_img)
cv.waitKey(0)


#black image for testing
gray_img = numpy.zeros([559, 559, 3], dtype=numpy.uint8)
gray_img.fill(5)

darker_img = cv.addWeighted(img_j, 0.4, gray_img, 0.1,0)
cv.imshow('FLEG logo - Darkened', darker_img)
cv.waitKey(0)


