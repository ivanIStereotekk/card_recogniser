import cv2 as cv2
import os

# -=imread=- 1arg - Picture path ,
# -=IMREAD_GRAYSCALE=- -method reading
# - в RGB — cv2.IMREAD_COLOR
# cv2.waitKey()
diam_10 = cv2.imread('pics/diamond-10.jpeg', cv2.IMREAD_GRAYSCALE)
heart_A = cv2.imread('pics/heart-a.jpeg.jpeg', cv2.IMREAD_GRAYSCALE)
k_pik = cv2.imread('pics/k-pika.jpeg.jpeg', cv2.IMREAD_GRAYSCALE)
pik_4 = cv2.imread('pics/pika-4.jpeg.jpeg', cv2.IMREAD_GRAYSCALE)
pik_5 =cv2.imread('pics/pika-5.jpeg', cv2.IMREAD_GRAYSCALE)
pik_Q = cv2.imread('pics/pika-q.jpeg', cv2.IMREAD_GRAYSCALE)



def loading_displaying_saving():
    img = cv2.imread('pics/diamond-10.jpeg', cv2.IMREAD_GRAYSCALE)
    cv2.imshow('diamond10', img)
    cv2.waitKey(0)
    cv2.imwrite('gray_d10.jpg', img)


loading_displaying_saving()