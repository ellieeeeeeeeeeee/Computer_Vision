import cv2
import numpy as np
import mediapipe as mp
import cvzone
from cvzone import HandDetector
import time
import math

cap = cv2.VideoCapture(0)
pTime = 0

run = True

while run:
    success, img = cap.read()

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img, f"FPS:{str(int(fps))}", (20, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)
    
    cv2.imshow("bob", img)
    key = cv2.waitKey(1)

    if key == ord('q'):
        run = False