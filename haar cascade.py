import cv2 #opencv 

sign1_cascade = cv2.CascadeClassifier('sign1.xml') #model to detect sign
sign2_cascade = cv2.CascadeClassifier('sign2.xml') #model to detect sign

cap = cv2.VideoCapture(0) #camera initialize

while True:
    iscameraopened, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    sign1 = sign1_cascade.detectMultiScale(gray, 1.1, 5)
    for (x,y,w,h) in sign1:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
        print('traffic sign detected')

    sign2 = sign2_cascade.detectMultiScale(gray, 1.3, 5)
    for (ex,ey,ew,eh) in sign2:
          cv2.rectangle(img,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
          print('traffic sign detected')

    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()