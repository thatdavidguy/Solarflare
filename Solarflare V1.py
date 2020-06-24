# imports

#imports cv2 (image processing that works together with numPy)
import cv2 
from PIL import ImageTk,Image
#numPy is a very effective library at handling lists (like images (lists of RGB values))
import numpy as np
#for testing how long the program runs look for print("--- %s seconds ---" % (time.time() - start_time))
import time
#Python User Interface (UI) building module
import tkinter as tk

#Function that finds the contours
def start_contour(lightdark):
    #resetting the text for other messages to appear
    label.configure(text ="")
    
    #start timer
    start_time = time.time()

    #if the link string is not empty
    if not(link == "") :
        #try except is an excellent way to work around/with errors
        try:
            #set message
            label.configure(text ="Press enter to close the images",fg = "black")
            #open image as normal
            norm = cv2.imread(link)

            #allimage is a variable that tells us if we should check the full image or just part of it
            if "allimage" in globals() and allimage == False:
                try:
                    #checks which coordinate is larger
                    if len(norm[0]) > 500 and len(norm): #> 500 and len(norm[0]) > len(norm):
                        proportionx = int (len(norm[0]) / (500 * (len(norm[0]) / len(norm))))
                        proportiony = int (len(norm) / (500))
                    """elif len(norm[0]) > 500 and len(norm) > 500 and len(norm[0]) < len(norm):
                        proportiony = int (len(norm) / (500 * (len(norm[0]) / len(norm))))
                        proportionx = int (len(norm[0]) / (500))"""
                    if xone > xtwo and not(xone == xtwo):
                        xlarge = xone
                        xsmall = xtwo
                    elif xone < xtwo and not(xone == xtwo):
                        xlarge = xtwo
                        xsmall = xone
                    else:
                        label.configure(text ="Cannot crop image to a single point",fg = "red")
                    
                    if yone > ytwo and not(yone == ytwo):
                        ylarge = yone
                        ysmall = ytwo
                    elif yone < ytwo and not(yone == ytwo):
                        ylarge = ytwo
                        ysmall = yone
                    else:
                        label.configure(text ="Cannot crop image to a single point",fg = "red")
                    #since the image on tkinter is scaled down we need to scale it up
                    xlarge = int(xlarge*proportionx)
                    xsmall = int(xsmall*proportionx)
                    ylarge = int(ylarge*proportiony)
                    ysmall = int(ysmall*proportiony)

                    #the cropping
                    newnum = norm[ysmall:ylarge]
                    finnum = []
                    for i in newnum:
                        finnum.append(i[xsmall:xlarge])
                    finnum = np.array(finnum)
                    norm = finnum
                except Exception as e:
                    print(e)
            #find the grayscale of the image
            gray = cv2.cvtColor(norm, cv2.COLOR_BGR2GRAY)
            #find average value of grayscale
            average = np.average(gray)
            #check if user added in sensitivity option (will return error if no input)
            try:
                sensitivity_value = sensitivity.get()
                #finding the "new" average according to sensitivity
                average = float(average) *float(sensitivity_value)
            except Exception as e:
                #uncomment line below to see what error would pop up
                #print(e)
                pass
            #set pixels to black(0) or white(1) if they meet a certain threshhold
            th, threshed = cv2.threshold(gray,average,255, cv2.THRESH_BINARY)#|cv2.THRESH_OTSU)
            #check if user wants to check for light or dark (it reverses the binary)
            if lightdark:
                threshed = cv2.bitwise_not(threshed)
            #Find the contours of this new black and white image
            contours, hierarchy = cv2.findContours(threshed,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
            #Print amount of contours found (total)
            print("amount of contours, ", len(contours))

            #default settings of size (edit according to your liking)
            size1 = 55  #minimal size (get rid of just singular pixels)
            size2 = len(norm[0]) * len(norm) #(get rid of background objects)
            
            #check for either input in settings (similar method to sensitivity)
            try:
                size1 = int(area_entry_min.get())
                print("size1 is",size1)
            except Exception as e:
                #uncomment line below to see what error would pop up
                #print(e)
                pass
            try:
                size2 = int(area_entry_max.get())
                print("size2 is",size2)
            except Exception as e:
                #uncomment line below to see what error would pop up
                #print(e)
                pass

            #adds all contours into the list newcontours (stores as a tuple the x,y coordinates of each contours)
            newcontours = [] 
            #applies the size threshholds on the contours
            for contour in contours: 
                if size1 <= cv2.contourArea(contour) < size2: 
                    print("Size of countour: ",cv2.contourArea(contour))
                    newcontours.append(contour)

            #Print out the amount of contours after the size check
            print("amount of contours after threshold, ", len(newcontours))
            #draw the contours 
            norm = cv2.drawContours(norm, newcontours, -1, (0,255,0), 1)
            #display both images for comparison.
            #Do note that ENTER must be pressed to continue using the UI
            cv2.imshow('contours drawn',norm)
            cv2.imshow('threshold applied',threshed)
            #Display time it took to run the program
            print("--- %s seconds ---" % (time.time() - start_time))
            #Waits for the Enter key and continues. Note, you can input time in the waitkey in the () as miliseconds
            cv2.waitKey(0)
            #gets rid of the windows
            cv2.destroyAllWindows()
        #incase any error in program
        except Exception as e: 
            #uncomment to check for error
            print(e)
            label.configure(text ="Please enter a valid image name!",fg = "red")
    else:
        label.configure(text ="Please enter in a image name!",fg = "red")

#Opens settings. TOPLEVEL is a new tab for tkiner UI
def opentoplevel():
    #prevents user from opening two setting tabs
    try :
        if tk.Toplevel.winfo_exists(toplevel) == 1:
            label.configure(text ="Please use one setting tab at a time!",fg = "red")
        else:
            opensettings()
    except Exception as e:
        #uncomment to check for error
        #print(e)
        opensettings()
        
#Opens area. TOPLEVEL is a new tab for tkiner UI     
def openarealevel():
    #prevents user from opening two area tabs
    try :
        if tk.Toplevel.winfo_exists(areatoplevel) == 1:
            alert.configure(text ="Please use one area tab at a time!",fg = "red")
        else:
            alert.configure(text ="")
            area()
    except Exception as e:
        alert.configure(text ="")
        #uncomment to check for error
        #print(e)
        area()

#function that gets called to open the area configuration tab
def area():
        global buttonareaoneadvice,buttonareatwoadvice,areatoplevel
        areatoplevel = tk.Toplevel()
        areatoplevel.title("Area Select")

        buttonareaoneadvice = tk.Label(areatoplevel,text = "")
        buttonareaoneadvice.pack()

        try:
            buttonareaoneadvice.configure(text =oneadvice,fg = "black")
        except:
            pass
    
        buttonareaone = tk.Button(areatoplevel,text = "First coordinate",command= lambda: posit(1))
        buttonareaone.pack()

        buttonareatwoadvice = tk.Label(areatoplevel,text = "")
        buttonareatwoadvice.pack()

        try:
            buttonareatwoadvice.configure(text =twoadvice,fg = "black")
        except:
            pass

        buttonareatwo = tk.Button(areatoplevel,text = "Second coordinate",command= lambda: posit(2))
        buttonareatwo.pack()

        buttonareatwo = tk.Button(areatoplevel,text = "Delete all coordinates",command= lambda: delline(True))
        buttonareatwo.pack()


#function that gets called to open the setting tab
def opensettings():
    #global variables called to be used across functions
    global area_entry_min,area_entry_max,sensitivity,label,toplevel,sensitivitylabeladvice,alert
    #opens toplevel
    toplevel = tk.Toplevel()
    toplevel.title("Settings")

    #places in all the widgets in the settings tab
    areaminlabel = tk.Label(toplevel,text = "Minimum area (px)")
    areaminlabel.pack()

    area_entry_min = tk.Entry(toplevel)
    area_entry_min.pack()

    areamaxlabel = tk.Label(toplevel,text = "Maximum area (px)")
    areamaxlabel.pack()

    area_entry_max = tk.Entry(toplevel)
    area_entry_max.pack()

    sensitivitylabel = tk.Label(toplevel,text = "Sensitivity (multiplier of average)")
    sensitivitylabel.pack()

    sensitivitylabeladvice = tk.Label(toplevel,text = "")
    sensitivitylabeladvice.pack()
    #suggest values for sensitivity 
    try:
        sensitivitylabeladvice.configure(text =inputtextsuggestion,fg = "black")
    except:
        pass

    sensitivity = tk.Entry(toplevel)
    sensitivity.pack()

    alert = tk.Label(toplevel,text = "")
    alert.pack()

    buttonarea = tk.Button(toplevel,text = "Open area select",command= openarealevel)
    buttonarea.pack()

#position finder of the click and this just findsand draws lines on the canvas(tkinter)
def posit(number):
    def clicked(event):
        global xone,xtwo,yone,ytwo,oneadvice,twoadvice,lineone,linetwo,linethree,linefour
        if number == 1:
            xone = event.x
            yone = event.y
            oneadvice = "The first coordinate is (" + str(xone) +"," + str(yone) + ")"
            buttonareaoneadvice.configure(text =oneadvice,fg = "black")
        elif number == 2:
            xtwo = event.x
            ytwo = event.y
            twoadvice = "The second coordinate is (" + str(xtwo) + "," + str(ytwo) + ")"
            buttonareatwoadvice.configure(text =twoadvice,fg = "black")
        if ("xone" in globals() and "xtwo" in globals() and "yone" in globals() and "ytwo" in globals()):
            try:
                canvasdisplay.delete(lineone)
                canvasdisplay.delete(linetwo)
                canvasdisplay.delete(linethree)
                canvasdisplay.delete(linefour)
            except Exception as e:
                pass
            delline(False)
            lineone = canvasdisplay.create_line(xone, yone, xtwo, yone,fill = "red")
            linetwo = canvasdisplay.create_line(xtwo, yone, xtwo, ytwo,fill = "red")
            linethree = canvasdisplay.create_line(xtwo, ytwo, xone, ytwo,fill = "red")
            linefour = canvasdisplay.create_line(xone, ytwo, xone, yone,fill = "red")
    canvasdisplay.bind("<Button-1>", clicked)

#function to delete lines on the canvas(tkinter) and also control the value of allimage
def delline(sure):
    global allimage
    if sure:
        allimage = True
        try:
            canvasdisplay.delete(lineone)
            canvasdisplay.delete(linetwo)
            canvasdisplay.delete(linethree)
            canvasdisplay.delete(linefour)
        except:
            pass
    else:
        allimage = False




#For better understanding on what kind of sensitivity should be used on the image
def click(key):
    #global variables to be used across functions
    global link,inputtextsuggestion
    #What you typed in the entry widget
    link = linkentry.get() + key.char
    #display image when it is typed in
    try:
        norm = cv2.imread(link)
        image_tk = cv2.cvtColor(norm, cv2.COLOR_BGR2RGB)
        image_tk = Image.fromarray(norm)
        if len(norm[0]) > 500 and len(norm): # > 500 and len(norm[0]) > len(norm):
            proportion = len(norm[0]) / len(norm)
            canvasdisplay.config(width=int(500 * proportion), height=500)
            image_tk = image_tk.resize((int(500 * proportion),500), Image.ANTIALIAS)
        """elif len(norm[0]) > 500 and len(norm) > 500 and len(norm[0]) < len(norm):
            proportion = len(norm[0]) / len(norm)
            image_tk = image_tk.resize((500,int(500*proportion)), Image.ANTIALIAS)
         """   
        image_tk = ImageTk.PhotoImage(image_tk)
        canvas_dis = canvasdisplay.create_image((0,0),image = image_tk,anchor="nw")
        canvasdisplay.canvas_dis = image_tk
        canvasdisplay.update()
    except Exception as e:
        pass

    #Try to find and calculate the recommended sensitivity
    try:
        #opens image 
        forsens = cv2.imread(link,0)
        #find average,25% precentile and 75% precentile
        average = np.average(forsens)
        lower = np.percentile(forsens,25)
        upper = np.percentile(forsens,75)
        #calculate sensitivity
        suggestup = upper/average
        suggestdown = lower/average
        #display sensitivity
        inputtextsuggestion =  str(suggestdown) +" to " + str(suggestup)+" for 25% to 75%"
        sensitivitylabeladvice.configure(text =inputtextsuggestion,fg = "black")
    except Exception as e:
        #uncomment to check for error
        #print(e)
        pass


#Set up what you see when you run the program (original tab)
root = tk.Tk()
root.title("Contour finder")
#variables
x = 0
y = 0
link = ""

#Set up widgets
linkentry = tk.Entry(root)
linkentry.pack()
#bind the entry widget to run the function click upon any characters inputed
linkentry.bind("<Key>", click)

global canvasdisplay
canvasdisplay = tk.Canvas(root)
canvasdisplay.pack()


button = tk.Button(root,text = "find (lighter) spots!",command= lambda: start_contour(False))
button.pack()

button = tk.Button(root,text = "find (darker) spots!",command= lambda: start_contour(True))
button.pack()

button2 = tk.Button(root,text = "Settings",command=opentoplevel)
button2.pack()

label = tk.Label(root,text = "")
label.pack()

#waits until the original tab is closed
root.mainloop()
