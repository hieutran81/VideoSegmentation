from color_histogram import *

SHOT_THRESHOLD = 1500000

def detect_shot(list_diff):
    prev = 0
    list_shot = []
    print(type(list_diff))
    for i in range(1, len(list_diff)):
        if (list_diff[i] >= SHOT_THRESHOLD):
            list_shot.append([prev, i])
            prev = i+1
    if (prev != len(list_diff)):
        list_shot.append([prev, len(list_diff)])
    print(list_shot)
    return list_shot

def write_shot():
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    out = cv2.VideoWriter('video/output.avi', fourcc, 20.0, (1280, 720))
    # out = cv2.VideoWriter('output.avi', -1, 20.0, (640, 480))
    for j in range(len(list_shot)):
        fourcc = cv2.VideoWriter_fourcc(*'MJPG')
        shot_name = "video/segment/run_now_"+str(j+1)+".avi"
        out = cv2.VideoWriter(shot_name, fourcc, 20.0, (1280,                                                                                                                                                                                                                                                                                                                                   720))
        for i in range(list_sho                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  t[j][0], list_shot[j][1]):
            print(list_frames[i].shape)
            out.write(list_frames[i])
        out.release()

list_diff = hist_difference()
list_shot = detect_shot(list_diff)
                                                                                                                                                                                                if __name__ == "__main__":
                                                                                                                                                                                                    write_shot()