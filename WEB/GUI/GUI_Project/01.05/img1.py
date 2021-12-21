import argparse
import cv2

parser = argparse.ArgumentParser()
parser.add_argument('--path', default='C:\\Users\\Public\\Lena.png', help='Image path.')
params = parser.parse_args()

img = cv2.imread(params.path)

print('original image shape : ', img.shape)

width, height = 128, 256
resized_img = cv2.resize(img,(width, height))
print('resized to 128x256 image shape : ', resized_img.shape)

w_mult, h_mult = 0.25, 0.5
resized_img = cv2.resize(img, (0,0), resized_img, w_mult, h_mult)
print('image shape : ', resized_img.shape)

w_mult, h_mult = 2, 4
resized_img = cv2.resize(img, (0,0), resized_img, w_mult, h_mult, cv2.INTER_NEAREST)
print('image shape : ', resized_img);

img_flip_along_x = cv2.flip(img, 0)
img_flip_along_x_along_y = cv2.flip(img_flip_along_x, 1)
img_flip_along_xy = cv2.flip(img, -1)