from server.utils.image_assembler import image_assembler
import cv2

#frame_info = {0:{'type':'owl', 'says':'bark'},1:{'type':'cat','says':'meow'}}
frame_info = {0: {'says': 'hello', 'type': 'unicorn'}, 1: {'says': 'meow', 'type': 'cat'}}
img = image_assembler.assemble(frame_info)
print (img)
