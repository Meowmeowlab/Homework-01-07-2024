# 1.Các phương pháp thay đổi mức sáng, thay đổi độ tương phản, tạo
# ảnh âm bản và phân ngưỡng ảnh. Thử nghiệm với ảnh 24 bit.

import os
import cv2 as cv
import sys
from Extra_Module.brightnessNcontrast import basicLinearTransform, gammaCorrection,adjustBrightnessContrast
from Extra_Module.negative import negative
from Extra_Module.threshold import basic_threshold,adaptive_threshold
from matplotlib import pyplot as plt

print(sys.version)

image_path = os.path.join('.','testimg','meow_400p.jpg')
img = cv.imread(image_path)

cv.imshow("Original Image",img)

img_brightness = img
img_gamma = img

alpha = 1.0
alpha_max = 500
beta = 0
beta_max = 200
gamma = 1.0
gamma_max = 200

def on_linear_transform_alpha_trackbar(val):
    global alpha
    alpha = val / 100
    showlinear()

def on_linear_transform_beta_trackbar(val):
    global beta
    beta = val - 100
    showlinear()

def on_gamma_correction_trackbar(val):
    global gamma
    gamma = val / 100
    img_gamma = gammaCorrection(img, gamma)
    cv.imshow("Gamma correction",img_gamma)

def showlinear():
    img_brightness = basicLinearTransform(img,alpha,beta)
    cv.imshow("Brightness and contrast adjustments", img_brightness)

def weightedLinearTransform():
    img_weighted = adjustBrightnessContrast(img, weightAlpha,weightBeta,weightGamma)
    cv.imshow("Weighted Img", img_weighted)
    
cv.namedWindow('Brightness and contrast adjustments')
cv.namedWindow('Gamma correction')
cv.namedWindow('Weighted Img')

alpha_init = int(alpha *100)
cv.createTrackbar('Alpha gain (contrast)', 'Brightness and contrast adjustments', alpha_init, alpha_max, on_linear_transform_alpha_trackbar)
beta_init = beta + 100
cv.createTrackbar('Beta bias (brightness)', 'Brightness and contrast adjustments', beta_init, beta_max, on_linear_transform_beta_trackbar)
gamma_init = int(gamma * 100)
cv.createTrackbar('Gamma correction', 'Gamma correction', gamma_init, gamma_max, on_gamma_correction_trackbar)
cv.imshow("Negative Image", negative(img))


weightBeta = 0
weightAlpha = 1
weightGamma = 0
def weighted_alpha_track_bar(val):
    global weightBeta
    weightBeta = val/100
    weightedLinearTransform()
def weighted_beta_track_bar(val):
    global weightAlpha
    weightAlpha = val/100
    weightedLinearTransform()
def weighted_gamma_track_bar(val):
    global weightGamma
    weightGamma = val
    weightedLinearTransform()

cv.createTrackbar('Alpha gain (contrast)', 'Weighted Img', 0, 200, weighted_alpha_track_bar)
cv.setTrackbarMin('Alpha gain (contrast)', 'Weighted Img', -100)
cv.createTrackbar('Beta bias', 'Weighted Img', 100, 200, weighted_beta_track_bar)
cv.createTrackbar('Gamma correction (brightness)', 'Weighted Img', 0, 200, weighted_gamma_track_bar)
cv.setTrackbarMin('Gamma correction (brightness)', 'Weighted Img', -100)

weightedLinearTransform()
cv.waitKey(0)



img_threshold = basic_threshold(img, 130, None, 1)

basicInvert = 1
minThres = 0
maxThres = 255

def minThreshold(val):
    global minThres
    minThres = val
    showBasicThreshold()

def maxThreshold(val):
    global maxThres
    maxThres = val
    showBasicThreshold()

def basicInvertToggle(val):
    global basicInvert
    # if(val == 1): basicInvert = True
    # else: basicInvert = True
    basicInvert = val
    # print("invert: ",val)
    showBasicThreshold()

def showBasicThreshold():
    img_threshold = basic_threshold(img,minThres,maxThres,basicInvert)
    cv.imshow("Threshold",img_threshold[1])

cv.namedWindow('Threshold')
cv.createTrackbar('Min Threshold', 'Threshold', minThres, 255, minThreshold)
cv.createTrackbar('Max Threshold', 'Threshold', maxThres, 255, maxThreshold)
cv.createTrackbar('Invert', 'Threshold', 0, 1, basicInvertToggle)
cv.imshow("Threshold",img_threshold[1])

img_adaptive_threshold = adaptive_threshold(img, 11, 3, None, 0, 0)
blockSize = 11
CVt = 3
gauFilter = 0
adaptiveInvert = 0
def blockSizeTracker(val):
    global blockSize
    blockSize = val
    if(val == 1 or val == 0):
        blockSize = val = 3 
    if (val%2)==0:
        blockSize = val+1
        cv.setTrackbarPos('Block Size', 'Adaptive Threshold', blockSize)
    showAdaptive()

def CValueTracker(val):
    global CVt
    CVt = val
    showAdaptive()

def gauToggle(val):
    global gauFilter
    gauFilter = val
    showAdaptive()

def adaptiveInvertToggle(val):
    global adaptiveInvert
    adaptiveInvert = val
    showAdaptive()

def showAdaptive():
    img_adaptive_threshold = adaptive_threshold(img, blockSize, CVt, None, adaptiveInvert, gauFilter)
    cv.imshow("Adaptive Threshold",img_adaptive_threshold)

cv.namedWindow('Adaptive Threshold')
cv.createTrackbar('Block Size', 'Adaptive Threshold', blockSize, 51, blockSizeTracker)
cv.createTrackbar('C Value', 'Adaptive Threshold', CVt, 51, CValueTracker)
cv.createTrackbar('Invert', 'Adaptive Threshold', 0, 1, adaptiveInvertToggle)
cv.createTrackbar('Gaussian Filter', 'Adaptive Threshold', 0, 1, gauToggle)
cv.imshow("Adaptive Threshold",img_adaptive_threshold)

cv.waitKey(0)
cv.destroyAllWindows()
#Made by Team meow meow

