import cv2
import mediapipe as mp
import cvzone
from cvzone.HandTrackingModule import HandDetector
import time
import numpy as np

cap = cv2.VideoCapture(0)

imgBG = cv2.imread("Pong\Background2.png", cv2.IMREAD_UNCHANGED)
imgGameOver = cv2.imread("Pong\gameOver.png")
imgBall = cv2.imread("Pong\Ball.png", cv2.IMREAD_UNCHANGED)
imgBat1 = cv2.imread("Pong\Bat1.png", cv2.IMREAD_UNCHANGED)
imgBat2 = cv2.imread("Pong\Bat2.png", cv2.IMREAD_UNCHANGED)

detector = HandDetector(detectionCon = 0.7, maxHands = 2)


pTime = 0
ballPos = [200, 200]
speedX = 10
speedY = 10
gameOver = False
score = [0,0]

run = True
cap.set(3,1280)
cap.set(4,720)
while run:
    _, img = cap.read()
    img = cv2.flip(img, 1)
    img = cv2.resize(img, (1280, 720))

    hands, img = detector.findHands(img, draw=True, flipType= False)

    #img = cv2.addWeighted(img, 0.3, imgBG, 0.9, 0)

    if hands:
        for hand in hands:
            x, y, w, h = hand['bbox']
            w1, h1, _ = imgBat1.shape
            y1 = y - h1//2
            y1 = np.clip(y1, 20, 430)

            if hand['type'] == 'Left':
                img = cvzone.overlayPNG(img, imgBat1, (60, y1))
                if 59 <ballPos[0] <59 + w1 and y1 < ballPos[1] < y1 + h1:
                    speedX = -speedX
                    ballPos[0] += 30
                    score[0] += 1

            if hand['type'] == 'Right':
                img = cvzone.overlayPNG(img, imgBat2, (1190, y1))
                if 1145 <ballPos[0] <1145 + w1 and y1 < ballPos[1] < y1 + h1:
                    speedX = -speedX
                    ballPos[0] -= 30
                    score[1] += 1

    if ballPos[0] < 40 or ballPos[0] > 1200:
        gameOver = True

    if gameOver:
        img = imgGameOver
        cv2.putTest(img, str(score[1] + score[0]).zfill(2), (585, 360), cv2.FONT_HERSHEY_COMPLEX, 2.5, (200, 0, 200), 5)
    if ballPos[1]>=600 or ballPos[1] <= 10:
        speedY = -speedY 

    ballPos[0] += speedX
    ballPos[1] += speedY

    img = cvzone.overlayPNG(img, imgBall, ballPos)

    cv2.putText(img, str(score[0]), (300, 650), cv2.FONT_HERSHEY_COMPLEX, 3, (255, 255, 255), 5)
    cv2.putText(img, str(score[1]), (900, 650), cv2.FONT_HERSHEY_COMPLEX, 3, (255, 255, 255), 5)


    cv2.imshow("Pong", img)
    key = cv2.waitKey(1)

    if key == ord('q'):
        run = False
    if key == ord('r'):
        ballPos[100, 100]
        speedX = 10
        speedY = 10
        gameOver = Falsescore = [0,0]
        imgGameOver = cv2.imgread("Pong/gameover.png")