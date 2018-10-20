import cv2
import numpy as np
import os
import pickle

img_dict = {}
rootDir = './'
for dirName, subdirList, fileList in os.walk(rootDir):
    for fname in fileList:
        if ('.png' in fname and 'scaled' in fname):
            print(fname)
            name = fname.replace('.png', '')
            name = name.replace('cropped_', '')
            name = name.replace('binarized_', '')
            name = name.replace('scaled_', '')
            print (name)
            img = cv2.imread('./' + str(fname), 0)
            img_dict.update({name: img})

print (img_dict)

for i in img_dict:
    cv2.imshow('fig' , img_dict[i])
    cv2.waitKey(0)
    cv2.destroyAllWindows()

pickle.dump(img_dict, open('image_dictionary', 'wb'))