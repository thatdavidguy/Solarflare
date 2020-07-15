# Solarflare
Solarflare project is to try and determine the location of active regions found on the sun.

![alt text](https://github.com/thatdavidguy/Solarflare/blob/master/imagesforreadme/showimagecontours.png)

## Installation
1. Make sure you have a proper IDE(Integrated development environment) to run the code such as Visual Studio Code for python or python IDLE.
2. Simply download the zip file and make sure the python script is in the same file as the image you want to check.


## Dependencies 
Simply run the following in your terminal once you have downloaded the project:
```pip install -r dependencies.txt```


Or

Please be sure to have these python libraries installed links are included (most of these are using pip3 to install the library).
1. openCV
```$pip3 install opencv-python-headless ```
2. PIL
```$pip3 install pillow ```
3. Numpy 
```$pip3 install numpy ```
4. Tkinter
```$pip3 install tkinter ```

## Running the Code
1. Make sure the image you want to check and the code are in the same folder (make a new one if possible).
2. Launch the python code and a simple tab will open.
3. Just type in the name of your image with the ending(.png or .jpg) and it will show you the image with the threshold applied and another image with the contours draw. Check the python shell for the amount of contours found and drawn.

## Navigating the "app"
#### On the main tab you will encounter 4 things,
![alt text](https://github.com/thatdavidguy/Solarflare/blob/master/imagesforreadme/showimage.png)
1. Entry box.   
(enter the name of your image inside this entry box)
2. find (lighter) spots.   
(click this to find where the light spots are)
3. find (darker) spots.   
(click this to find where the dark spots are)
4. settings.   
(click this to open the settings tab)

#### Settings tab
![alt text](https://github.com/thatdavidguy/Solarflare/blob/master/imagesforreadme/showimagesettings.png)
1. minimum area.   
(enter minimum area a spot has to be)
2. maximum area.   
(enter maximum area a spot has to be)
3. sensitivity.   
(enter sensitivity of the program. The larger the sensitivity the more spots)
4. open area select.   
(click this to open the area tab)

#### area tab
![alt text](https://github.com/thatdavidguy/Solarflare/blob/master/imagesforreadme/showimagearea.png)
1. First coordinate.   
(click this and then on the image on displayed on the main tab to click your first coordinate)
2. Second coordinate.   
(click this and then on the image on displayed on the main tab to click your second coordinate)
3. Delete all coordinates.   
(click this to delete all coordinates)


#### created by 2 students (Keith and David)
