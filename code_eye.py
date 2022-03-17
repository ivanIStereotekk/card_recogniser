import cv2 as cv2
import os

#Набор фотографий игральных карт

diam_10 = cv2.imread('pics/diamond-10.jpeg', cv2.IMREAD_GRAYSCALE)
heart_A = cv2.imread('pics/heart-a.jpeg.jpeg', cv2.IMREAD_GRAYSCALE)
k_pik = cv2.imread('pics/k-pika.jpeg.jpeg', cv2.IMREAD_GRAYSCALE)
pik_4 = cv2.imread('pics/pika-4.jpeg.jpeg', cv2.IMREAD_GRAYSCALE)
pik_5 =cv2.imread('pics/pika-5.jpeg', cv2.IMREAD_GRAYSCALE)
pik_Q = cv2.imread('pics/pika-q.jpeg', cv2.IMREAD_GRAYSCALE)


img = cv2.imread('pics/diamond-10.jpeg', cv2.IMREAD_COLOR)
# IMREAD_GRAYSCALE - Image Read Gray Scale
'''Чтобы считать изображение в RGB — cv2.IMREAD_COLOR, в оттенках серого — cv2.IMREAD_GRAYSCALE. 
По умолчанию данный аргумент принимает значение cv2.IMREAD_COLOR. '''
def loading_displaying_saving():
    cv2.imshow('diamond10', img)
    '''i'm show'''
    cv2.waitKey(0)
    '''если мы далее не укажем функцию cv2.waitKey(), то изображение моментально закроется.
    # 0 - значит любая клавиша.'''
    #-------------------------------------------
    cv2.imwrite('gray_d10.jpg', img)
    '''cv2.imwrite() записываем изображение в файл в формате jpg
    поддерживает :png, tiff,jpeg,bmp и т. д'''
#--------------------------------------------
#важно помнить, что библиотека OpenCV хранит каналы формата RGB (B - G - R)в обратном порядке,
# в то время как мы думаем в терминах красного, зеленого и синего,
# то OpenCV хранит их в порядке синего, зеленого и красного цветов

def manipulate_pix():
    '''Для того, чтобы узнать высоту,
    ширину и количество каналов у изображения
    можно использовать атрибут shape:

'''
    print("Высота:" + str(img.shape[0]))
    print("Ширина:" + str(img.shape[1]))
    print("Количество каналов:" + str(img.shape[2]))

#loading_displaying_saving()

# manipulate_pix() №
def resizing():
    res_img = cv2.resize(img, (500, 900), cv2.INTER_NEAREST) #Nearest - interpolation (nearest Pixel)



'''
(b, g, r) = img[0,0] # Тут координаты х - горизонт /// у - вертикаль
print("Красный: {}, Зелёный: {}, Синий: {}".format(r, g, b))

img[0, 0] = (255, 0, 0)
(b, g, r) = img[0, 0]
print("Красный: {}, Зелёный: {}, Синий: {}".format(r, g, b))'''

#print(format(img))
img[10,10] = (255,0,0)
(b, g, r) = img[0,0]
# Тут координаты х - горизонт /// у - вертикаль
print("Красный: {}, Зелёный: {}, Синий: {}".format(r, g, b))

def colored():
    cv2.imshow(img)
