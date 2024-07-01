import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


def show_histogram_gray(img):
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    gray_hist = cv.calcHist([img_gray], [0], None,[256],[0,256])

    plt.figure()
    plt.title("Grayscale Histogram")
    plt.xlabel("Bins")
    plt.ylabel("# of pixel")
    plt.plot(gray_hist)
    plt.xlim([0,256])
    return plt

def show_histogram_color(img):
    plt.figure()
    plt.title("Color Histogram")
    plt.xlabel("Bins")
    plt.ylabel("# of pixel")

    #img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    colors = ("b","g","r")
    for i in range(3):
        hist = cv.calcHist([img], [i], None,[256],[0,256])
        plt.plot(hist, color=colors[i])
        plt.xlim([0,256])  
    return plt

def histogram_equalizer_color(img, option = "ycrcb"):
    global imgDst
    # if(option == "ycrcb"):
    # Convert color to YCrCb
    img_ycrcb = cv.cvtColor(img,cv.COLOR_BGR2YCrCb)
    # Equalize the histogram of the Y channel
    img_ycrcb[:, :, 0] = cv.equalizeHist(img_ycrcb[:, :, 0])
    # Convert back to RGB color-space from YCrCb
    imgDst = cv.cvtColor(img_ycrcb, cv.COLOR_YCrCb2BGR)

    if(option == "hsv"):
        # convert image from RGB to HSV
        img_hsv = cv.cvtColor(img, cv.COLOR_RGB2HSV)
        # Histogram equalisation on the V-channel
        img_hsv[:, :, 2] = cv.equalizeHist(img_hsv[:, :, 2])
        imgDst = cv.cvtColor(img_hsv, cv.COLOR_HSV2BGR)
    if(option == "yuv"):
        img_yuv = cv.cvtColor(img, cv.COLOR_BGR2YUV)
        # Equalize the histogram of the Y channel
        img_yuv[:,:,0] = cv.equalizeHist(img_yuv[:,:,0])
        imgDst = cv.cvtColor(img_yuv, cv.COLOR_YUV2BGR)



    # cv.imshow("mepow",imgDst)
    # cv.waitKey(0)
    return imgDst

def histogram_equalizer_gray(img):
    # Convert color to grayscale
    img_gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    # Equalize the gray channel on the image
    imgDst = cv.equalizeHist(img_gray) 
    return imgDst

def hist_match(source, template):
    """
    Adjust the pixel values of a grayscale image such that its histogram
    matches that of a target image

    Arguments:
    -----------
        source: np.ndarray
            Image to transform; the histogram is computed over the flattened
            array
        template: np.ndarray
            Template image; can have different dimensions to source
    Returns:
    -----------
        matched: np.ndarray
            The transformed output image
    """

    oldshape = source.shape
    source = source.ravel()
    template = template.ravel()

    # get the set of unique pixel values and their corresponding indices and
    # counts
    s_values, bin_idx, s_counts = np.unique(source, return_inverse=True,
                                            return_counts=True)
    t_values, t_counts = np.unique(template, return_counts=True)

    # take the cumsum of the counts and normalize by the number of pixels to
    # get the empirical cumulative distribution functions for the source and
    # template images (maps pixel value --> quantile)
    s_quantiles = np.cumsum(s_counts).astype(np.float64)
    s_quantiles /= s_quantiles[-1]
    t_quantiles = np.cumsum(t_counts).astype(np.float64)
    t_quantiles /= t_quantiles[-1]

    # interpolate linearly to find the pixel values in the template image
    # that correspond most closely to the quantiles in the source image
    interp_t_values = np.interp(s_quantiles, t_quantiles, t_values)

    return interp_t_values[bin_idx].reshape(oldshape)