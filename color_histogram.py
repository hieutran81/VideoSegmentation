from read_video import *
import cv2
import numpy as np
from matplotlib import pyplot as plt

def color_hist():
    # img = list_frames[0]
    #hist, bins = np.histogram(img.ravel(), 256, [0, 256])
    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2H)
    # print(gray)
    # print(gray.shape)
    #hist = cv2.calcHist([img], [0], None, [256], [0, 256])
    #print(hist)
    # print(type(hist))
    # print(hist.shape)
    list_hist = []
    for frame in list_frames:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        n_pixel = frame.shape[0] * frame.shape[1]
        # print(gray.shape)
        hist = cv2.calcHist([gray], [0], None, [16], [0, 256])
        # print(hist)
        hist = hist * (1.0/n_pixel)
        # print(hist)
        # print(hist.shape)
        # cv2.imwrite("video/image0.jpg", frame)
        list_hist.append(hist)
        # fig = plt.figure()
        # plt.hist(frame.ravel(), 256, [0, 256], color='blue')
        # fig.savefig("video/histogram.png")
        # plt.show()
    return list_hist

def hist_difference():
    list_diff = []
    accumulate_sum = []
    for i in range(len(list_hist) - 1):
        x = np.sum(np.abs(np.subtract(list_hist[i+1],list_hist[i])))
        list_diff.append(x)
        if (i==0):
            accumulate_sum.append(x)
        else:
            accumulate_sum.append(accumulate_sum[-1] + x)
        # print(x)
    # print(accumulate_sum)
    fig = plt.figure()
    plt.plot(list_diff)
    plt.show()
    fig.savefig("video/histogram.png")
    return list_diff, accumulate_sum

def get_video():
    return list_frames

list_frames =  read_video("video/run_now.avi")
list_hist = color_hist()
# hist_difference()