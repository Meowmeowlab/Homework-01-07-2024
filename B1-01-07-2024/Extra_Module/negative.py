import cv2 as cv

def negative(img):
    # Negate the original image 
    img_neg = 255 - img
    return img_neg