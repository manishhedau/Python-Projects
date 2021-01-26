import cv2
import numpy as np
from PIL import ImageGrab


def screenRecorder():
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi',fourcc,5.0,(1366,768)) # number in list is nothing but a resoluation of lopatop

    while True:
        img = ImageGrab.grab()
        img_np = np.array(img)

        frame = cv2.cvtColor(img_np,cv2.COLOR_BGR2RGB)
        cv2.imshow('SCREEN RECORDER ',frame)

        out.write(frame)

        # 27 is an keyboard code
        if cv2.waitKey(1) == 27:
            break


    out.release()
    cv2.destroyAllWindows()

screenRecorder()