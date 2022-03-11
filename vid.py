import cv2

cap = cv2.VideoCapture(0)
while 1:
    ret, img = cap.read()
    imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #cv2.imshow('grey',imgray)

    ret,thresh = cv2.threshold(imgray,100,255,0)
    cnts = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)[-2]

    cv2.drawContours(img,cnts,-1,(0,0,255),3)
    img = cv2.resize(img,(350,250),interpolation = cv2.INTER_CUBIC)
    thresh = cv2.resize(thresh,(350,250),interpolation = cv2.INTER_CUBIC)

    cv2.imshow('out',img)
    cv2.imshow('thresh',thresh)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv2.waitKey(0)
