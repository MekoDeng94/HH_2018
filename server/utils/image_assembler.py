import os
import numpy as np
import cv2
import pickle


class image_assembler(object):

    @staticmethod
    def assemble(frame_info, save_path=None):
        img_dic = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'image_dictionary')

        image_dictionary = pickle.load(open(img_dic, 'rb'))
        foreground = image_dictionary[frame_info[0]['type']]
        flip_foreground = cv2.flip(image_dictionary[frame_info[1]['type']], 1)
        space = np.empty((384, 60))
        space.fill(255)
        foreground = np.hstack((foreground, space))
        foreground = np.hstack((foreground, flip_foreground))
        background = cv2.imread("scene.png", 0)
        alpha = np.zeros((384,384))
        flip_alpha = np.zeros((384, 384))
        alpha = np.hstack((alpha, space - 255))
        alpha = np.hstack((alpha, flip_alpha))
        print (foreground.shape)
        print (alpha.shape)
        for i in range (0, foreground.shape[0]):
            for j in range (0, foreground.shape[1]):
                if foreground[i, j] != 255:
                    alpha[i, j] = 255

        for i in range (0, flip_foreground.shape[0]):
            for j in range (0, flip_foreground.shape[1]):
                if flip_foreground[i, j] != 255:
                    flip_alpha[i, j] = 255

        right_splice_bound = int (background.shape[1]/2)+414
        left_splice_bound = int (background.shape[1]/2)-414
        top_splice_bound = int (background.shape[0]/2)+0
        bottom_splice_bound = int (background.shape[0]/2)+384

        print (foreground.shape)
        print (alpha.shape)
        slice = background[top_splice_bound:bottom_splice_bound, left_splice_bound:right_splice_bound]
        print(slice.shape)
        slice = slice - alpha

        for i in range (0, slice.shape[0]):
            for j in range (0, slice.shape[1]):
                if slice[i, j] < 0:
                    slice[i,j] = foreground[i, j]

        background[top_splice_bound:bottom_splice_bound, left_splice_bound:right_splice_bound] = slice
        background = cv2.resize(background, (720, 509), interpolation=cv2.INTER_AREA)
        cv2.imwrite('final_frame.png', background)
        return 'final_frame.png'
        # cv2.imshow('fig', background)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()