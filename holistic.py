import cv2
import mediapipe as mp
import cvzone
import time

cap = cv2.VideoCapture(0)
pTime = 0

mpPose = mp.solutions.pose
pose = mpPose.Pose()
mpDraw = mp.solutions.drawing_utils
mpDrawStyle = mp.solutions.drawing_styles


run = True

while run:
    success, img = cap.read()
    results = pose.process(img)

    if results.pose_landmarks:
        mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h, w, c = img.shape
            cx, cy = int(lm.x *w), int(lm.y *h)
            if id > 0 and id <11:
                cv2.circle(img, (cx, cy), 3, (255, 0, 180), cv2.FILLED)
            if id > 10 and id <25:
                cv2.circle(img, (cx, cy), 3, (0, 255, 0), cv2.FILLED)
            if id > 25 and id <33:
                cv2.circle(img, (cx, cy), 3, (0, 180, 255), cv2.FILLED)
            

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img, f"FPS:{str(int(fps))}", (20, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)
    
    cv2.imshow("bob", img)
    key = cv2.waitKey(1)

    if key == ord('q'):
        run = False