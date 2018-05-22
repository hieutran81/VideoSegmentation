
from shot_boundary import *
from color_histogram import *


def detect_keyframe(start,end):
    return int((start+end)/2)

def get_keyframes():
    key_frames = []
    for i in range(len(list_shot)):
        start = list_shot[i][0]
        end = list_shot[i][1]
        x = detect_keyframe(start,end)
        key_frames.append(x)
    return key_frames

def write_keyframes(key_frames):
    for i in range(len(key_frames)):
        key_name = "video/segment/run_now_"+str(i+1)+".jpg"
        cv2.imwrite(key_name,list_frames[key_frames[i]])


if __name__  == "__main__":
    key_frames = get_keyframes()
    write_keyframes(key_frames)
