import cv2
import cvzone
from cvzone.ColorModule import ColorFinder
import numpy as np
import math


## Initialize the Video
cap = cv2.VideoCapture('Videos/vid (1).mp4')

## Create the color Finder object
## If we put False there is no debug mode and we are running the debug mode,
## we are trying to find the color with a trackbar value 
myColorFinder = ColorFinder(False)
## hsvVals='red' 
hsvVals = {'hmin': 8, 'smin': 96, 'vmin': 115, 'hmax': 14, 'smax': 255, 'vmax': 255}

## Variables
posListX, posListY  = [], []
## for each of these value we are going to find the corresponding value. 
XList = [item for item in range(0, 1300)]
prediction=False


while True:
    ## Grab the image
    success, img = cap.read()
    ## img = cv2.imread('Ball.png')
    img = img[0: 900, :]
    
    ## Find the Color Ball
    imgColor, mask = myColorFinder.update(img, hsvVals)

    ## Find location of the Ball
    imgContours, contours = cvzone.findContours(img, mask, minArea=500)
    
    if contours:
        posListX.append(contours[0]['center'][0])
        posListY.append(contours[0]['center'][1])
        ## print(cx, cy)
     
    if posListX: 
        ## Find the coefficients
        A, B, C = np.polyfit(posListX, posListY, 2)
        ## This will give A, B, C equation and based on this equation we can plot a line and predict on what's going.
        
        for i, (posX, posY) in enumerate(zip(posListX, posListY)):
            pos =(posX, posY)
            cv2.circle(imgContours, pos, 10, (0, 255, 0), cv2.FILLED)
            ## It is showing for the current frame  
            if i == 0:
                cv2.line(imgContours, pos, pos, (0, 255, 0), 5)
            else: 
                cv2.line(imgContours, pos, (posListX[i-1],posListY[i-1]), (0, 255, 0), 2)
                
        for x in XList:
            y = int(A*x**2 +B*x + C)
            cv2.circle(imgContours, (x, y), 2, (255, 0, 255), cv2.FILLED)
            
        if len(posListX)<10:
            ## Prediction
            ## x values 330 to 440 y value. We input the value of y and we get the value of x.   
            a  = A
            b  = B 
            c = C-590
            x = int(-b -math.sqrt(b**2-(4*a*c)))/(2*a) 
            prediction = 330<x<430
    
        if prediction:
            cvzone.putTextRect(imgContours, "Basket", (50, 100), 
                               scale=5, thickness=5, colorR=(0, 200, 0), offset=20)
            
        else:
            cvzone.putTextRect(imgContours, "No Basket", (50, 100), scale=5, 
                               thickness=5, colorR=(0, 0, 200), offset=20)
        
        
        
            
            
    ## Polynomial Regression y = Ax^2 + Bx + C, For any given x you can find a value of y.
                
    ## Displaying 
    imgContours = cv2.resize(imgContours, (0, 0), None, 0.7, 0.7) ## None as output and now give the scale
    ## img = cv2.resize(img, (0, 0), None, 0.7, 0.7)
    
    cv2.imshow('ImageColor', imgContours)
    
    if cv2.waitKey(10) & 0XFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
    
    

    

    

