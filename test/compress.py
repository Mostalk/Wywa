import cv2

img = cv2.imread("TK7D9uBMdLA.jpg")
cv2.imwrite("compressed.jpg", img, [int(cv2.IMWRITE_JPEG_QUALITY), 10]);
