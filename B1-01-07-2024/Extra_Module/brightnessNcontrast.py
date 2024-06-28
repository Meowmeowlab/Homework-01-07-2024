import cv2 as cv
import numpy as np


def basicLinearTransform(img,alpha:float,beta:float):
    res = cv.convertScaleAbs(img, alpha=alpha, beta=beta)
    # img_corrected = cv.hconcat([img, res])
    # img_dst = cv.imshow("Brightness and contrast adjustments", img_corrected)
    return res

def gammaCorrection(img,gamma:float):
    ## [changing-contrast-brightness-gamma-correction]
    lookUpTable = np.empty((1,256), np.uint8)
    for i in range(256):
        lookUpTable[0,i] = np.clip(pow(i / 255.0, gamma) * 255.0, 0, 255)
    res = cv.LUT(img, lookUpTable)
    
    ## [changing-contrast-brightness-gamma-correction]
    # img_gamma_corrected = cv.hconcat([img, res])
    # img_dst = cv.imshow("Gamma correction", img_gamma_corrected)
    return res