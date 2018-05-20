

import numpy as np
import cv2

def read_video(video_name):
    list_frames = []
    cap = cv2.VideoCapture(video_name)
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret:
            #cv2.imshow('frame',frame)
            # print(frame.shape)
            list_frames.append(frame)
            break
            # print("hieuvodoi")
        else:
            print("hieu ba dao")
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    return list_frames

read_video("video/00202.MTS")
