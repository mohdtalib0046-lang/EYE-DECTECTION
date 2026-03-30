import cv2
import mediapipe as mp
import pygame

pygame.mixer.init()
pygame.mixer.music.load("audio2.mp3")

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh()

cap = cv2.VideoCapture(0)

alarm_on = False

while True:
    ret, frame = cap.read()
    if not ret:
        break

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb)

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:

            top = face_landmarks.landmark[159].y
            bottom = face_landmarks.landmark[145].y

            eye_distance = abs(top - bottom)

            # 👁️ Eyes Closed
            if eye_distance < 0.02:

                cv2.rectangle(frame,(50,50),(590,430),(0,0,255),5)
                cv2.putText(frame,"EYES CLOSED",(180,40),
                            cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3)

                if not alarm_on:
                    pygame.mixer.music.play(-1)
                    alarm_on = True

            # 👁️ Eyes Open
            else:

                cv2.rectangle(frame,(50,50),(590,430),(0,255,0),5)
                cv2.putText(frame,"EYES OPEN",(200,40),
                            cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),3)

                if alarm_on:
                    pygame.mixer.music.stop()
                    alarm_on = False

    cv2.imshow("Eye Alert System", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()