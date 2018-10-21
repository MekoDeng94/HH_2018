from server.utils.image_assembler import image_assembler
import cv2

frame_info = {0:{'type':'owl', 'says':'bark'},1:{'type':'cat','says':'meow'}}
img = image_assembler.assemble(frame_info)
cv2.imshow('fig', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
