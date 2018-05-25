from color_histogram import *

SHOT_THRESHOLD = 1000000


def calc_threshold():
    global shot_threshold, soft_threshold, cut_threshold
    max_threshold = 0
    id_peak = 0
    for i in range(len(list_diff)):
        if (list_diff[i] > max_threshold):
            max_threshold = list_diff[i]
            id_peak = i
    mean_diff = np.mean(np.array(list_diff))
    std_diff = np.std(np.array(list_diff))
    soft_threshold = mean_diff + 5.0 * std_diff
    print("shoft threshold: ", soft_threshold)
    print(std_diff)
    print(mean_diff)
    if (mean_diff < max_threshold * 0.5):
        shot_threshold = max_threshold * 0.5
        print(shot_threshold)
    cut_threshold = max_threshold * 0.75

def sum_between(a,b):
    if (a == 0):
        return accumulate_sum[b]
    return accumulate_sum[b] - accumulate_sum[a-1]

def detect_shot_one_threshold(list_diff):
    prev = 0
    start = -1
    list_shot = []
    for i in range(0, len(list_diff)):
        if (i < prev):
            continue
        if (list_diff[i] >= shot_threshold):
            if (i - prev < 10):
                continue
            list_shot.append([prev, i])
            prev = i+1
            start = -1
        # if ( (start > -1) and (list_diff[i] < soft_threshold)):
        #     if (sum_between(start,i) > shot_threshold):
        #         if (i - prev < 10):
        #             continue
        #         # print(list_diff[start:i + 1])
        #         list_shot.append([prev,i])
        #         prev = i+1
        #         start = -1
        if ( (start == -1) and (list_diff[i] > soft_threshold) ):
            start = i
    if (prev != len(list_diff)):
        list_shot.append([prev, len(list_diff)])
    print(list_shot)
    return list_shot


def detect_shot_two_threshold(list_diff):
    prev = 0
    start = -1
    list_shot = []
    for i in range(0, len(list_diff)):
        if (i < prev):
            continue
        if (list_diff[i] >= cut_threshold ):
            if (i - prev < 10):
                continue
            list_shot.append([prev, i])
            prev = i+1
            start = -1
        if ( (start > -1) and (list_diff[i] < soft_threshold)):
            if (sum_between(start,i) > cut_threshold):
                if (i - prev < 10):
                    continue
                # print(list_diff[start:i + 1])
                list_shot.append([prev,i])
                prev = i+1
                start = -1
        if ( (start == -1) and (list_diff[i] > soft_threshold) ):
            start = i
    if (prev != len(list_diff)):
        list_shot.append([prev, len(list_diff)])
    print(list_shot)
    return list_shot


def write_shot():
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    # out = cv2.VideoWriter('video/output.avi', fourcc, 20.0, (1280, 720))
    # out = cv2.VideoWriter('output.avi', -1, 20.0, (640, 480))
    for j in range(len(list_shot)):
        fourcc = cv2.VideoWriter_fourcc(*'MJPG')
        shot_name = "video/segment1/run_now_0"+str(j+1)+".avi"
        out = cv2.VideoWriter(shot_name, fourcc, 20.0, (1280,  720))
        for i in range(list_shot[j][0], list_shot[j][1]+1):
            # print(list_frames[i].shape)
            out.write(list_frames[i])
        out.release()

list_diff, accumulate_sum = hist_difference()
calc_threshold()
list_shot = detect_shot_one_threshold(list_diff)
if __name__ == "__main__":
    write_shot()