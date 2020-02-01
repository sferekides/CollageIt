import cv2 as cv
import numpy
import os


def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv.imread(os.path.join(folder,filename))
        if img is not None:
            images.append(img)
    return images

stored_images = load_images_from_folder('Images_For_Hack')