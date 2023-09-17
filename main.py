import cv2
import face_recognition

feed = cv2.VideoCapture(0)

# function to draw yellow box around person
def drawbox(canvas, top, right, bottom, left):
    cv2.rectangle(canvas, (left, top), (right, bottom), (0, 255, 255), 1)

while True:
    ret, frame = feed.read()

    # detect faces
    face_locations = face_recognition.face_locations(frame)

    for location in face_locations:
        # draw box around face
        (top, right, bottom, left) = location
        drawbox(frame, top, right, bottom, left)

    cv2.imshow('live feed', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

feed.release()

cv2.destroyAllWindows()
