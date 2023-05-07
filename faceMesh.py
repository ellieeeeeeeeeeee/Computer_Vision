import cv2
import mediapipe as mp
import cvzone
import time

cap = cv2.VideoCapture(0)
pTime = 0

run = True

mpFaceMesh = mp.solutions.face_mesh
faceMesh = mpFaceMesh.FaceMesh(max_num_faces = 1, refine_landmarks = True)
mpDraw = mp.solutions.drawing_utils
drawingSpec = mpDraw.DrawingSpec(color=(0, 255, 0), thickness = 1, circle_radius = 2)

while run:
    success, img = cap.read()
    results = faceMesh.process(img)

    if results.multi_face_landmarks:
        for faceLms in results.multi_face_landmarks:
            mpDraw.draw_landmarks(img, faceLms, mpFaceMesh.FACEMESH_CONTOURS, drawingSpec, drawingSpec)
            for id, lm in enumerate(faceLms.landmark):
                ih, iw, ic = img.shape
                x, y = int(lm.x *iw), int(lm.y *ih)
                print('id: ' + str(id), end='  ')
                print('x: ' + str(x), end='  ')
                print('y: ' + str(y), end='  ')
                if id == 145 or id == 374:
                    cv2.circle(img, (x, y), 10, (0, 0, 255), cv2.FILLED)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img, f"FPS:{str(int(fps))}", (20, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)
    
    cv2.imshow("bob", img)
    key = cv2.waitKey(1)

    if key == ord('q'):
        run = False