import numpy as np
import cv2
import os
import create_folder as cf
import time
#import test as t


def open_camera(where):
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    currentFrame = 0
    start=time.time()
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            frame = cv2.flip(frame, 1)
            name = where+"\\"+str(currentFrame) + '.jpg'
            print(name)
            cv2.imwrite(name, frame)
            print(frame)
            cv2.imshow('frame', frame)
            currentFrame += 1
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
        if(time.time()-start>5):
            break;
    cap.release()

    cv2.destroyAllWindows()
    return(True)

