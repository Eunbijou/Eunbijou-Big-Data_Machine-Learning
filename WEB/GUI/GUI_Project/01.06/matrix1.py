import cv2
import numpy as np

image = cv2.imread('C:\\Users\\Public\\Lena.png')
print('Shape : ', image.shape)
print('Data Type : ', image.dtype)

cv2.imshow('image', image)
cv2.waitKey()
cv2.destroyAllWindows()

image = image.astype(np.float32) / 255
print('Shape : ', image.shape)
print('Data Type : ', image.dtype)

cv2.imshow('Image', np.clip(image * 2, 0, 1))
cv2.waitKey()
cv2.destroyAllWindows()

image = (image * 255).astype(np.uint8)
print('Shape : ', image.shape)
print('Data Type : ', image.dtype)

cv2.imshow('Image', image)
cv2.waitKey()
cv2.destroyAllWindows()