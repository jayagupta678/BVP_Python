import cv2
face_data = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
image = cv2.imread("img_1.png", cv2.IMREAD_COLOR)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
dataset = face_data.detectMultiScale(image)
for x,y,w,h in dataset:
    cv2.rectangle(image, (x,y), (x+w, y+h), (0,0,255), 2 )
cv2.imwrite('result.jpg', image)
