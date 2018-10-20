import cv2
import numpy as np
import os

rootDir = './'
for dirName, subdirList, fileList in os.walk(rootDir):
    for fname in fileList:
        if ('.png' in fname and 'binarized' in fname and 'cropped' not in fname and 'scene' not in fname):
            img = cv2.imread(fname, 0)
            sumx = np.sum(img, axis=0)
            sumy = np.sum(img, axis=1)
            idx = np.where(sumx < 255*img.shape[0]-256)[0]
            idy = np.where(sumy < 255*img.shape[1]-256)[0]
            top_bound = 0
            low_bound = img.shape[0]
            left_bound = 0
            right_bound = img.shape[1]
            idx[idx.shape[0]-1] = idx[idx.shape[0]-2]-1
            idy[idy.shape[0]-1] = idy[idy.shape[0]-2]-1
            top_bound = np.min(idy)
            low_bound = np.max(idy)
            left_bound = np.min(idx)
            right_bound = np.max(idx)


            crop_img = img[top_bound:low_bound, left_bound:right_bound]
            cv2.imwrite('cropped_' + str(fname), crop_img)