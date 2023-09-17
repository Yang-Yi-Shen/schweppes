import cv2

feed = cv2.VideoCapture(0)

while True:
    ret, frame = feed.read()
  
    cv2.imshow('live feed', frame)
      
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

feed.release()

cv2.destroyAllWindows()