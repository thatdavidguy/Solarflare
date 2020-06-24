# Solarflare
Solarflare project is to try and determine the location of solarflares found on the sun.

## Installation
1. Make sure you have a proper IDE(Integrated development environment) to run the code such as Visual Studio Code for python or python IDLE.
2. Open the code by clicking the raw button on github found above and download/copy the code or any another way you can download the code.

## Dependencies 
1. Please be sure to have these python libraries installed links are included (most of these are using pip3 to install the library).
1.1 openCV
    pip3 install opencv-python-headless
2. PIL
    pip3 install pillow
3. Numpy 
    pip3 install numpy
4. Tkinter
    pip3 install tkinter

## Running the Code
1. Make sure the image you want to check and the code are in the same folder (make a new one if possible).
2. Launch the python code and a simple tab will open.
3. Just type in the name of your image with the ending(.png or .jpg) and it will show you the image with the threshold applied and another image with the contours draw. Check the python shell for the amount of contours found and drawn.

## Navigating the "app"
##### On the main tab you will encounter 4 things,
Entry box
(enter the name of your image inside this entry box)
find (lighter) spots 
(click this to find where the light spots are)
find (darker) spots 
(click this to find where the dark spots are)
settings
(click this to open the settings tab)

###### Settings tab
minimum area
(enter minimum area a spot has to be)
maximum area
(enter maximum area a spot has to be)
sensitivity
(enter sensitivity of the program. The larger the sensitivity the more spots)
open area select
(click this to open the area tab)

###### area tab
First coordinate
(click this and then on the image on displayed on the main tab to click your first coordinate)
Second coordinate
(click this and then on the image on displayed on the main tab to click your second coordinate)
Delete all coordinates
(click this to delete all coordinates)

#### created by 2 students (Keith and David)
