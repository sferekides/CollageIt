CollageIt

Created by: Kendall Willis, Greg Garret, Dominic A., Savvas Ferekides

After you have read through this file there is a to-do list at the end. Given how late I am staying up I don't think that I will make it by 8am. I likely will be back around 9 or 10 but hope that you all will make progress whilst I sleep.

Notes on how to run ReadImage.py and any subsequent files:
1) I use VSCode as I have said before.
2) For now - git clone into the repo (preferably somewhere good like your Desktop)
3) in the file explorer of VSCode open the repository folder wherever you have it on your laptop (Desktop is good)
3.5) If you type Ctrl + ~ the terminal window should pop up (some of the things I describe below will use the terminal and this built-in terminal is really easy to use)
4) You should now see the files that I created in the Repo including this file
5) Make sure that you have Python installed on your computer - any version is fine I think
6) Install any helpers that VSCode suggests when you open ReadImage.py
7) run pip install opencv-python (this installs opencv on your commputer)
7.5) I believe at this point you should be able to run the programs without issue
8) ***most important***
The following command is what I use to run the Python program (there is also a play button that pops up in the upper right corner that you can push to run the code)
You will have to change the directories to match where python is in your computer and where you have stored this repository
C:/Python/Python38-32/python.exe "c:/Users/Savvas Ferekides/Desktop/CollageIt/ReadImage.py"
9) After running the program windows should pop up and you should see some logos. Now take a look at the comments and code that are in ReadImage.py to figure out more about how we will be editing and configuring image files

Notes on OpenCV:
Follow the ReadImage.py files and its respective comments to learn how to edit images
It will start with an ordinary file and show you how you can change them using various methods
Some of these techniques will be useful to us

I am sleep deprived and it is almost 3am.
Am I ~Hackerman yet?
If the fleg logo wore pants would it go on the bottom 2 gears or halfway up the gear?

Some ideas I have had for how to display words:
Basically, if a pixel has 3 values each for RGB respectively, the color black would be represented by the sum of the max (255)
of those values (765). Depending on how many pixels you have, you can add all these values together and and find a value that represents the whole image. If the image was all black and 100px then the value of all of these sums would be  76,500. If the image was all white and 100px then the value of these sums would be 0. The midpoint of these values could be used as the line over which we will divide white and black values. These images should then be sorted for ease of the next step.
Furthermore, If you are writing in white on top of a black background you could take the whitest images (those that are first on the low end of the sorted list) and use those for your words. If you know the word that you are creating you should know the number of images you will need and can select those images. After this, you should randomize the order of the images that are left over to make the background seem more blended. Then create your image. If there is not enough contrast then you can perhaps brighten those images that you are writing with and also apply a blur to those images that you are using as the background to make even more of a contrast. 
(I showed this to Greg and Kendall before they left)



To-do:
1) Loop for loading images from another folder in which they are stored. I DO NOT want to have this folder in the repo. We DO NOT need to be moving these images around.
2) Loop determining the values of the images based on color, and sorting them. This might require object, but you should probably ask one of the mentors that has experience with python or images about how they would go about sorting them with a new value that you create for them based on the RGB values.
3) Someone needs to figure out how to stitch these images together. My idea is that you could probably do it with a 2-d array but this will likely require more than that.
4) Someone needs to determine how we are going to size the letters and position them on the image. Start with an image compiled with a set number of images and a test value of 'FLEG'. We can figure out an extendable algorithm after  
