import os
import numpy as np
import cv2
import pickle


class image_assembler(object):

    @staticmethod
    def assemble(frame_info, save_path=None):
        img_dic = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'image_dictionary')

        image_dictionary = pickle.load(open(img_dic, 'rb'))
        print(image_dictionary)
        frame = image_dictionary[frame_info[0]['type']]
        flip_img = cv2.flip(image_dictionary[frame_info[1]['type']], 1)
        space = np.empty((256, 60))
        space.fill(255)
        frame = np.hstack((frame, space))
        frame = np.hstack((frame, flip_img))
        background = cv2.imread(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'binarized_scene.png'), 0)
        right_splice_bound = int (background.shape[1]/2)+286
        left_splice_bound = int (background.shape[1]/2)-286
        top_splice_bound = int (background.shape[0]/2)-78
        bottom_splice_bound = int (background.shape[0]/2)+178
        background[top_splice_bound:bottom_splice_bound, left_splice_bound:right_splice_bound] = frame
        background = cv2.resize(background, (720, 509), interpolation=cv2.INTER_AREA)
        output_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'output.png')
        if save_path:
            output_file_path = os.path.join(save_path, 'output.png')
        cv2.imwrite(output_file_path, background)
        return 'output.png'