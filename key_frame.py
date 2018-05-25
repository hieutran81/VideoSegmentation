
from shot_boundary import *
from color_histogram import *
SIMILAR_THRESHOLD = 0.1

def cal_distance(x,y):
    # print(np.sum(np.abs(np.subtract(x,y))))
    return np.sum(np.abs(np.subtract(x,y)))


def detect_median_keyframe(start,end):
    return int((start+end)/2)

def detect_mean_keyframe(start,end):
    # print(list_hist.shape)
    shot = list_hist[start:end+1]
    shot = np.array(shot)
    print(shot.shape)
    avg = np.average(shot, axis=0)
    # print(avg)
    # print(avg.shape)
    min_dis = 100000000000
    key_frame = 0
    for i in range(start,end+1):
        if (cal_distance(avg, list_hist[i])  < min_dis):
            min_dis = cal_distance(avg, list_hist[i])
            key_frame = i
    print(key_frame)
    return key_frame

def detect_mode_keyframe(start,end):
    max_similar_frame = 0
    key_frame = 0
    print(start, end)
    for i in range(start+1 , end):
        count = 0
        for j in range(start+1,end):
            if (cal_distance(list_hist[i], list_hist[j])  < SIMILAR_THRESHOLD):
                print(cal_distance(list_hist[i], list_hist[j]))
                count = count + 1
        # print(count)
        if (count > max_similar_frame):
            print(i)
            print(count)
            max_similar_frame = count
            key_frame = i
    print(key_frame)
    return key_frame


def get_keyframes():
    key_frames = []
    for i in range(len(list_shot)):
        start = list_shot[i][0]
        end = list_shot[i][1]
        x = detect_mean_keyframe(start,end)
        key_frames.append(x)
    return key_frames

def write_keyframes(key_frames):
    for i in range(len(key_frames)):
        key_name = "video/two_threshold/mean_"+str(i+1)+".jpg"
        cv2.imwrite(key_name,list_frames[key_frames[i]])

if __name__  == "__main__":
    key_frames = get_keyframes()
    write_keyframes(key_frames)
