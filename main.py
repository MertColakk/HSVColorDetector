#Library
import cv2
import numpy as np

#Read Camera
cap = cv2.VideoCapture(0)
cv2.namedWindow("Camera")

#Empty FNC for Trackbar
def empty(x):
    pass

#Create Trackbars
cv2.createTrackbar("Lower-H","Camera",0,180,empty)
cv2.createTrackbar("Lower-S","Camera",0,255,empty)
cv2.createTrackbar("Lower-V","Camera",0,255,empty)

cv2.createTrackbar("Upper-H","Camera",0,180,empty)
cv2.createTrackbar("Upper-S","Camera",0,255,empty)
cv2.createTrackbar("Upper-V","Camera",0,255,empty)

#Set Upper's Value to Max
cv2.setTrackbarPos("Upper-H","Camera",180)
cv2.setTrackbarPos("Upper-S","Camera",255)
cv2.setTrackbarPos("Upper-V","Camera",255)

#Create infinite loop bcs videos are pictures what is saved frame by frame :)
while True:
    #Read Data
    success,frame = cap.read()

    #Flip the original frame
    frame = cv2.flip(frame,1)

    #Convert frame to hsv
    if not success:
        break
    #Conver to hsv
    frameHSV = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    #Get Values
    lowerH = cv2.getTrackbarPos("Lower-H","Camera")
    lowerS = cv2.getTrackbarPos("Lower-S","Camera")
    lowerV = cv2.getTrackbarPos("Lower-V","Camera")

    upperH = cv2.getTrackbarPos("Upper-H", "Camera")
    upperS = cv2.getTrackbarPos("Upper-S", "Camera")
    upperV = cv2.getTrackbarPos("Upper-V", "Camera")

    #Create NumPy Arrays for inRange FNC
    lowerHSV = np.array([lowerH,lowerS,lowerV])
    upperHSV = np.array([upperH,upperS,upperV])

    #Change the frame
    mask = cv2.inRange(frameHSV,lowerHSV,upperHSV)

    #Show the mask and Open Camera
    cv2.imshow("Camera", frame)
    cv2.imshow("Mask",mask)

    #Exit if presses 'q'
    if cv2.waitKey(20) &0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


