import cv2
import os

rootDir = './'
for dirName, subdirList, fileList in os.walk(rootDir):
    for fname in fileList:
        if ('.png' in fname and 'binarized' not in fname):
            img = cv2.imread(fname, 0)
            for i in range (img.shape[0]):
                for j in range (img.shape[1]):
                    if img[i, j] < 128:
                        img[i, j] = 0
                    else:
                        img[i, j] = 255
            cv2.imwrite('binarized_' + str(fname), img)