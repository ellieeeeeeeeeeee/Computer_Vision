import cv2
import mediapipe as mp
import cvzone
import time

cap = cv2.VideoCapture(0)
pTime = 0

mpHandDetection = mp.solutions.hands
handDetection = mpHandDetection.Hands(max_num_hands=2, min_detection_confidence=0.1, min_tracking_confidence=0.1)
mpDraw = mp.solutions.drawing_utils

run = True

while run:
    success, img = cap.read()
    results = handDetection.process(img)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                # print(id, lm)
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                if id == 0:
                    print(id, cx, cy)
                    cv2.circle(img, (cx, cy), 10, (255, 0, 180), cv2.FILLED)
                if id == 4:
                    cv2.circle(img, (cx, cy), 10, (255, 0, 0), cv2.FILLED)
                if id == 8:
                    cv2.circle(img, (cx, cy), 10, (0, 255, 0), cv2.FILLED)
                if id == 12:
                    cv2.circle(img, (cx, cy), 10, (0, 255, 255), cv2.FILLED)
                if id == 16:
                    cv2.circle(img, (cx, cy), 10, (0, 180, 255), cv2.FILLED)
                if id == 20:
                    cv2.circle(img, (cx, cy), 10, (0, 0, 255), cv2.FILLED)

                mpDraw.draw_landmarks(img, handLms, mpHandDetection.HAND_CONNECTIONS)

    cv2.putText(img, f"FPS:{str(int(fps))}", (20, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)
    
    cv2.imshow("bob", img)
    key = cv2.waitKey(1)

    if key == ord('q'):
        run = False
