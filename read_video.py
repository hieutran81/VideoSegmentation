import numpy as np
import cv2

def read_video(video_name):
    list_frames = []
    cap = cv2.VideoCapture(video_name)
    print("hieuvodoi")
    count = 0
    while(cap.isOpened()):
        ret, frame = cap.read()
        #print(frame.shape)
        if ret:
            #cv2.imshow('frame',frame)
            # print(frame.shape)
            count = count +1
            list_frames.append(frame)
            if count >= 10000:
                break
            #break
            # print("hieuvodoi")
        else:
            print("hieu ba dao")
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    return list_frames
def play_video(video_name, start_play, finish_play):
    cap = cv2.VideoCapture(video_name)
    print("hieuvodoi")
    count = 0
    while(cap.isOpened()):
        ret, frame = cap.read()
        #print(frame.shape)
        if ret:
            if (count >= start_play):
                cv2.imshow('frame',frame)
            print(frame.shape)
            count = count +1
            if (count > finish_play):
                 break
            #break
            # print("hieuvodoi")
        else:
            print("hieu ba dao")
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()




#play_video("video/run_now.avi",199, 205)
# play_video("video/output.avi",0,100)

if __name__ == "__main__":
    play_video("video/output.avi", 0, 100)