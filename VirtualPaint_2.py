import cv2
import numpy as np
import time
import os
import HandTrackingModule as htm 

###############
brushThickness = 30
eraser = 100
#############
pTime = 0
cTime = 0


#webcam size
cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)
detector = htm.handDetector(detectionCon=0.85)

#detector = htm.handDetector(detectionCon = 0.85)
folderPath = "Header"
mylist = os.listdir(folderPath)
print(mylist)

overlayList = []
for imPath in mylist:
    image = cv2.imread(f'{folderPath}/{imPath}')
    overlayList.append(image)
print(len(overlayList))
header = overlayList[0]
drawColor = (204,255,229)

xp,yp = 0,0

#creating a new canvas for drawing
imgCanvas = np.zeros((720,1280,3),np.uint8)

while True:
    # 1)implimenting webcam and importing image
    retu, img = cap.read()
    img = cv2.flip(img,1) #flipping image

    # 2.Find Landmarks
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)

    if len(lmList)!=0:

        #print(lmList)

        #tip of index and middle fing
        x1,y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]

        # 3.check which finger is up
        fingers = detector.fingersUp()
        #print(fingers)


        # 4.selection Mode-2 fingers up
        if fingers[1] and fingers[2]:
            xp, yp = 0, 0
            #print("Selection Mode")

            #checking for clicks
            if y1 < 125:
                if 250 < x1 < 450:
                    header = overlayList[0]#clicking purple dot
                    drawColor = (255, 0, 255)#purple
                elif 550 < x1 < 750:
                    header = overlayList[0]#clicking blue dot
                    drawColor = (255, 0, 0) #blue
                elif 800 < x1 < 950:
                    header = overlayList[0]#clicking green dot
                    drawColor = (0, 255, 0)#green
                elif 1050 < x1 < 1200: # clicking Eraser
                    header = overlayList[0]
                    drawColor = (0, 0, 0) #black
            cv2.rectangle(img, (x1, y1 - 25), (x2, y2 + 25),drawColor, cv2.FILLED)


        # 5.draw Mode = 1 finger up
        if fingers[1] and fingers[2] == False:
            cv2.circle(img, (x1, y1), 15, drawColor, cv2.FILLED)
            print("Drawing Mode")
            if xp ==0 and yp ==0:
                xp, yp = x1, y1

            # used to increase size of eraser
            if drawColor == 0:
                cv2.line(img, (xp, yp), (x1, y1), drawColor, eraser)
                cv2.line(imgCanvas, (xp, yp), (x1, y1), drawColor,eraser)
            else:
                cv2.line(img, (xp, yp), (x1, y1), drawColor, brushThickness)
                cv2.line(imgCanvas, (xp, yp), (x1, y1), drawColor, brushThickness)

            xp, yp = x1, y1

    imgGray = cv2.cvtColor(imgCanvas,cv2.COLOR_BGR2GRAY)
    _, imgInv = cv2.threshold(imgGray,50,255,cv2.THRESH_BINARY_INV)
    imgInv = cv2.cvtColor(imgInv,cv2.COLOR_GRAY2BGR)
    img = cv2.bitwise_and(img, imgInv)
    img = cv2.bitwise_or(img, imgCanvas)


    #setting header image
    img[0:128,0:1280]=header #added image size

     #blend the image and canvas(it is bit transperent)
    #img = cv2.addWeighted(img,0.5,imgCanvas,0.5,0)


    cv2.imshow("Canvas",imgCanvas)
    cv2.imshow("Inv", imgInv)
    cv2.imshow("image", img)
    if cv2.waitKey(1) & 0xFF == ord('a'):
        break



