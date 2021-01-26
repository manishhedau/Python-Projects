import cv2

imgCapture = cv3.VideoCapture(0)
result = True

while result:
    ret,frame = imgCapture.read()
    cv2.imwrite('test.jpg',frame)
    result = False
    print('Done ... Image capture')

imgCapture.release()