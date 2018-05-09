import cv2
camera = cv2.VideoCapture(0)
camera1= cv2.VideoCapture(0)
while True:
    return_value,image = camera.read()
    return_value,image1 = camera1.read()
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    gray1 = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    cv2.rectangle(gray,(0,0),(256,240),(0,255,0),3)
    cv2.rectangle(gray,(0,0),(256,479),(0,255,0),3) 
    cv2.imshow('image',gray)
    cv2.imshow('image1',gray1)
    if cv2.waitKey(1)& 0xFF == ord('s'):
        cv2.imwrite('test.jpg',image)
        cv2.imwrite('test1.jpg',image1)
        break
camera.release()
camera1.release()
cv2.destroyAllWindows()
