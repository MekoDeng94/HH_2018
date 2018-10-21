import os
import numpy as np
import cv2
import pickle


class image_assembler(object):

    @staticmethod
    def assemble(frame_info):        
        image_dictionary = pickle.load('image_dictionary', 'rb')
        #print (image_dictionary)
        frame = image_dictionary[frame_info[0]['type']]
        flip_img = cv2.flip(image_dictionary[frame_info[1]['type']], 1)
        space = np.empty((256, 60))
        #print (space.shape)
        space.fill(255)
        #print (space.shape)
        #print (frame.shape)
        frame = np.hstack((frame, space))
        frame = np.hstack((frame, flip_img))
        background = cv2.imread('binarized_scene.png', 0)
        right_splice_bound = int (background.shape[1]/2)+286
        left_splice_bound = int (background.shape[1]/2)-286
        top_splice_bound = int (background.shape[0]/2)-78
        bottom_splice_bound = int (background.shape[0]/2)+178
        background[top_splice_bound:bottom_splice_bound, left_splice_bound:right_splice_bound] = frame
        background = cv2.resize(background, (720, 509), interpolation=cv2.INTER_AREA)
        return background