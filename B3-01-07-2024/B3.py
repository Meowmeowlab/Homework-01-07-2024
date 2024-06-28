import os
import cv2 as cv
from Extra_Module.noisyspclr import add_sp_clr

image_path = os.path.join('.','testimg','meow_400p.jpg')
img = cv.imread(image_path)

noise_percent = 0
img_salt_pepper = add_sp_clr(img,0.02)

k_size = 3
img_blur = cv.blur(img_salt_pepper,(k_size,k_size))
img_gblur = cv.GaussianBlur(img_salt_pepper,(k_size,k_size),5)
img_mblur = cv.medianBlur(img_salt_pepper,k_size)
imgDenoise = cv.fastNlMeansDenoisingColored(img_salt_pepper,None,k_size,k_size,7,21)


def showBlurFilter():
    img_salt_pepper = add_sp_clr(img, float(noise_percent/100))

    # img_blur = cv.blur(img_salt_pepper,(k_size,k_size))
    # img_gblur = cv.GaussianBlur(img_salt_pepper,(k_size,k_size),5)
    img_mblur = cv.medianBlur(img_salt_pepper,k_size)
    # imgDenoise = cv.fastNlMeansDenoising(img_salt_pepper,None,21,7,3)
    # imgDenoise = cv.fastNlMeansDenoisingColored(img_salt_pepper,None,k_size,k_size,7,21)

    cv.imshow("Original Image",img)
    cv.imshow("Noise Salt Pepper",img_salt_pepper)
    # cv.imshow("DeNoise Box Blur",img_blur)
    # cv.imshow("DeNoise Gaussian Blur",img_gblur)
    cv.imshow("DeNoise Mean Blur",img_mblur)
    # cv.imshow("Native OpenCV DeNoiser",imgDenoise)

def onNoiseAddingTrackbar(val):
    global noise_percent
    noise_percent = val       
    showBlurFilter()

def onKSizeChange(val):
    global k_size
    if(val == 1 or val == 0):
        k_size = val = 3 
    if(val % 2 == 0):
        k_size = val + 1
    cv.setTrackbarPos('K Size', 'Noise Salt Pepper', k_size)
    showBlurFilter()

cv.namedWindow("Noise Salt Pepper")
cv.createTrackbar('Noise %', "Noise Salt Pepper", 2, 100, onNoiseAddingTrackbar)
cv.createTrackbar('K Size', "Noise Salt Pepper", 3, 90, onKSizeChange)
showBlurFilter()

cv.waitKey(0)
cv.destroyAllWindows()
#Made by Team meow meow