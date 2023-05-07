import cv2
import mediapipe as mp
import cvzone
import time

cap = cv2.VideoCapture(0)
pTime = 0

mpFaceDetection = mp.solutions.face_detection
mpDraw = mp.solutions.drawing_utils
faceDetection = mpFaceDetection.FaceDetection()

run = True

while run:
    success, img = cap.read()

    results = faceDetection.process(img)

    if results.detections:
        for id, detection in enumerate(results.detections):
            mpDraw.draw_detection(img, detection)
            print(id, detection)
            cv2.putText(img, f'{str(int(detection.score[0]*100))}%', (100,100), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img, f"FPS:{str(int(fps))}", (20, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)
    
    cv2.imshow("bob", img)
    key = cv2.waitKey(1)

    if key == ord('q'):
        run = False