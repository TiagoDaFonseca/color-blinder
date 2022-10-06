from spectral import open_image
import numpy as np
import cv2
from cv2 import GIGA

def isEmpty (a):
    if not a:
        return True
    return False

def Dir (filename):
    a = filename.split('/')
    b=[]
    s=''
    for i in range(len(a)-1):
        b.append(a[i])
    for item in b:
        s = s + item + '/'
    return s

def mean (x , y, data):
    t = np.array([])
    for index in range(data.shape[2]):
        t = np.append(t, np.mean(data[x-25:x+25,y-25:y+25, index]))
    #print(t.shape)
    return t
    '''
    sum_arr = np.array([])
    for index in range(data.shape[2]):
        sum = 0
        for index1 in range(x - 50, x + 50):
            for index2 in range(y - 50, y + 50):
                sum = sum + data[index1, index2, index]
                mean = sum / 10000
        sum_arr = np.append(sum_arr, mean)
    return sum_arr
    '''

#Hypercube functions

def read_data (f):
    img = open_image(f)
    return np.asarray(img.load())

def clear_data ():
    return None

def uint8_img (data):
    return np.require(data*255, dtype=np.uint8)

def blur_img (data, w):
    return cv2.blur(data,(w,w))

#Color functions

def save_colors (color1, color2, filename):
    w = 512
    h = 512

    blank_image = np.zeros((w, h, 3), np.uint8)
    blank_image[:, 0:w // 2] = color1  # (B, G, R)
    cv2.putText(blank_image, 'Master', (20, w - 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

    blank_image[:, w // 2:w] = color2
    cv2.putText(blank_image, 'Sample', (276, w - 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2,cv2.LINE_AA)
    print(filename)
    cv2.imwrite(filename+'.png', blank_image)



if __name__ == '__main__':
    a = None
    print(isEmpty(a))
