from tkinter import NO
import cv2 as cv
import matplotlib.pyplot as plt

def basic_threshold(img, min_thres: float | None, max_thres: float | None, invert: int):
    if(min_thres == None): min_thres = 256/2
    if(max_thres == None): max_thres = 230
    if(invert == 1): mode = cv.THRESH_BINARY
    else : mode = cv.THRESH_BINARY_INV

    img_gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    thres = cv.threshold(img_gray, min_thres,max_thres,mode)    
    return thres

def adaptive_threshold(img, block_size: int, C: float, max_thres: float | None, invert: int = 0, gaufilter: int = 0):
    if(max_thres == None): max_thres = 255
    if(invert == 0): mode = cv.THRESH_BINARY 
    else : mode = cv.THRESH_BINARY_INV
    if(gaufilter == 0): gau = cv.ADAPTIVE_THRESH_MEAN_C
    else : gau = cv.ADAPTIVE_THRESH_GAUSSIAN_C

    img_gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    thres = cv.adaptiveThreshold(img_gray, max_thres, gau, mode, block_size, C)
    #thres = cv.adaptiveThreshold(img_gray, max_thres, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
    return thres
