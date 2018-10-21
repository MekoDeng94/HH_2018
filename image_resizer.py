import cv2
import numpy as np
import os

rootDir = './'
for dirName, subdirList, fileList in os.walk(rootDir):
    for fname in fileList:
        if ('.png' in fname and 'cropped' in fname and 'scaled' not in fname):
            img = cv2.imread(fname, 0)
            r = 256.0 / img.shape[0]
            #print (r)
            dim = (int(img.shape[0] * r), 256)
            #print (dim)
            resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
            cv2.imshow('fig', resized)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            cv2.imwrite('scaled_' + str(fname), resized)
