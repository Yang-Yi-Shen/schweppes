import cv2
import face_recognition
from collections import deque
import math

feed = cv2.VideoCapture(0)

# function to draw yellow box around person
def drawbox(canvas, top, right, bottom, left):
    cv2.rectangle(canvas, (left, top), (right, bottom), (0, 255, 255), 1)

# function to get center of box
def getcenter(top, right, bottom, left):
    x = (left + right) // 2
    y = (top + bottom) // 2
    return x,y

dot_history = deque(maxlen=10)

while True:
    ret, frame = feed.read()

    # detect faces
    face_locations = face_recognition.face_locations(frame)

    for location in face_locations:
        # draw box around face
        (top, right, bottom, left) = location
        drawbox(frame, top, right, bottom, left)

        x, y = getcenter(top, right, bottom, left)
        dot_history.append((x, y))

    distances = []
    
    # track movement
    for i in range(len(dot_history)):
        x, y = dot_history[i]
        # draw dots
        cv2.circle(frame, (x, y), 1, (0, 0, 255), -1)

        # draw lines between the dots
        if i > 0:
            prev_x, prev_y = dot_history[i - 1]
            cv2.line(frame, (prev_x, prev_y), (x, y), (0, 0, 255), 1)

            # calculate change in position using pythagorean theorem
            distance = math.sqrt((x - prev_x)**2 + (y - prev_y)**2)
            # add to distance list
            distances.append(distance)
            # display distance above drawn line
            cv2.putText(frame, f'{distance:.2f}', (int((x + prev_x) / 2), int((y + prev_y) / 2) - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)

    # display average change between face positions
    if len(distances) > 0:
        average_distance = sum(distances) / len(distances)
        cv2.putText(frame, f'Average movement: {average_distance:.2f}', (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

    cv2.imshow('live feed', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

feed.release()

cv2.destroyAllWindows()
