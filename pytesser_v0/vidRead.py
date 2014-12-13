#much stuff got commented in the end, staying here for a while for educational reasons only
#need to add connection to video from robot
#add REGEX for not speaking nonsense
import numpy as np
from time import sleep
import cv2
from pytesser import *
from naoqi import ALProxy
import re

cap = cv2.VideoCapture(0)
#fgbg = cv2.BackgroundSubtractorMOG() 

#connecting to the robot
#IP = "192.168.0.238"
#speech module
#tts = ALProxy("ALTextToSpeech", IP, 9559)


while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    #sleep(5)

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #gray = cv2.GaussianBlur(gray, (5, 5), 0)
    gray = cv2.bilateralFilter(gray, 11, 10, 7)
    #grayCopy = gray
    #edged = cv2.Canny(grayCopy, 40, 200)
    #(contours, _) = cv2.findContours(edged, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #contours = sorted(contours, key = cv2.contourArea, reverse = True)[:5]
    #screenCnt = None
    #_,thresh = cv2.threshold(edged,127,255,0)
    #kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
    #dilated = cv2.dilate(thresh,kernel,iterations = 13) # dilate
    #fgmask = fgbg.apply(edged)
    #contours, hierarchy = cv2.findContours(edged,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    # Display the resulting frame
    #cv2.drawContours(gray, contours, -1, (0,255,0), 3)
   # for contour in contours:
    #    [x,y,w,h] = cv2.boundingRect(contour)
        #imageTest = image

     #discard areas that are too large
        #if h>600 and w>600:
         #   continue

     #discard areas that are too small
      #  if h<60 or w<60:
       #     continue

        #draw rectangle around contour on original image
        #cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,255),2)
    #cv2.drawContours(edged, [screenCnt], -1, (0, 255, 0), 3)
    cv2.imshow('frame',gray)
    image = Image.fromarray(gray)
    speech = image_to_string(image)
    for char in speech:
        #if char in [A-Z]:
        print char #writing to console
        #else:
         #   continue
    #robot speech
    #tts.say(speech)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()