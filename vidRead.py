#much stuff got commented in the end, staying here for a while for educational reasons only
#need to add connection to video from robot
import numpy as np
import vision_definitions
from time import sleep
import cv2
#from pytesser import *
from tesserwrap import Tesseract
from PIL import Image
from naoqi import ALProxy

ocr = Tesseract()
ocr.set_variable("tessedit_char_whitelist", "ABCDEFGHIJKLMNOPQRSTUVWXYZ") #since we use upper cased text only
#ocr.set_variable("classify_enable_learning", "0")
#ocr.set_variable("classify_enable_adaptive_matcher", "0")

#cap = cv2.VideoCapture(0)

#connecting to the robot
IP = "192.168.0.238"
#speech module
tts = ALProxy("ALTextToSpeech", IP, 9559)
cameraid=0
camProxy = ALProxy("ALVideoDevice", IP, 9559)
resolution = vision_definitions.kVGA
colorSpace = vision_definitions.kBGRColorSpace
videoClient = camProxy.subscribe("python_client", resolution, colorSpace, 5)
camProxy.setParam(vision_definitions.kCameraSelectID, cameraid)
#9137743885


while(True):
    # Capture frame-by-frame
    #ret, frame = cap.read()
    #image = cv2.imread('nao.png',cv2.CV_LOAD_IMAGE_GRAYSCALE)
    image = camProxy.getImageRemote(videoClient)
    #image = image[6]
    image = Image.fromstring("RGB", (image[0], image[1]), image[6])
    image = np.asarray(image)[:,:,::-1].copy()

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    #r = 1000.0 / image.shape[1]
    #dim = (1000, int(image.shape[0] * r))
    #print height, " ", width
    #sleep(5)
    #gray = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
    #height, width = gray.shape[:2]
    # Our operations on the frame come here, doing some manipulation to reduce effects from surrounding objects,
    #light&shadow play, etc 
    gray = cv2.medianBlur(gray, 5)
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.bilateralFilter(gray, 5, 25, 25)

    #cv2.rectangle(gray, (width/2-150, height/2-150), (width/2+200, height/2+150), (255,0,0), 2)

    cv2.imshow('frame',gray) #showing image
    #gray = gray.copy()[height/2-150:height/2+150,width/2-150:width/2+200]
    image = Image.fromarray(gray) #turning array into image
    speech = ocr.ocr_image(image) #ocr-ing image by Tesseract
    #print type(speech)
    #speech = ocr.get_utf8_text()
    if ocr.get_mean_confidence() >= 63 and len(speech.strip()) >1:
        tts.say(str(speech))
        print speech 
    sleep(1)
    #robot speech

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
#cap.release()
camProxy.unsubscribe(videoClient)
cv2.destroyAllWindows()