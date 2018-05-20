from read_video import *
import cv2

def color_hist():
    img = list_frames[0]
    #hist, bins = np.histogram(img.ravel(), 256, [0, 256])
    hist = cv2.calcHist([img], [0], None, [256], [0, 256])
    print(hist)



list_frames =  read_video("video/00202.MTS")