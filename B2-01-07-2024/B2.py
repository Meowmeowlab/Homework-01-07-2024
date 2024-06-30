import os
import cv2 as cv
from matplotlib import pyplot as plt
from Extra_Module.histogram import histogram_equalizer_color,histogram_equalizer_gray,show_histogram_color,show_histogram_gray

image_path = os.path.join('.','testimg','meow_400p.jpg')
img = cv.imread(image_path)

img_YCrCb_equalize = histogram_equalizer_color(img)
img_HSV_equalize = histogram_equalizer_color(img,"hsv")
img_YUV_equalize = histogram_equalizer_color(img,"yuv")
img_gray_equalize = histogram_equalizer_gray(img)

def showGraph(graph_img):
    gray_plt = show_histogram_gray(graph_img)
    color_plt = show_histogram_color(graph_img)
    gray_plt.show()
    color_plt.show()

    # ax = gray_plt.gca()
    # line = ax.lines[0]

    # ax_color = color_plt.gca()
    # line_color = ax_color.lines
    # print(ax_color)

    # plt.close("all")
    # # Three subplots sharing both x/y axes
    # f, (gray_plt, color_plt) = plt.subplots(2,sharex=True,sharey=True)
    # gray_plt.plot(line.get_xdata(), line.get_ydata())
    # gray_plt.set_title('Grayscale Histogram')

    # color_plt.plot(line_color[0].get_xdata(), line_color[0].get_ydata(),"b")
    # color_plt.plot(line_color[1].get_xdata(), line_color[1].get_ydata(),"g")
    # color_plt.plot(line_color[2].get_xdata(), line_color[2].get_ydata(),"r")
    # color_plt.set_title('Color Histogram')

    # # ax3.scatter(x, 2 * y ** 2 - 1, color='r')
    # # Fine-tune figure; make subplots close to each other and hide x ticks for
    # # all but bottom plot.
    # f.subplots_adjust(hspace=0.5)
    # #plt.setp([a.get_xticklabels() for a in f.axes[:-1]], visible=False)

    # plt.show()
    # plt.close("all")

cv.imshow("Original Image",img)
cv.imshow("HSV Color-space",img_HSV_equalize)
cv.imshow("YCrCb Color-space", img_YCrCb_equalize)
cv.imshow("YUV Color-space", img_YUV_equalize)
cv.imshow("Grayscale",img_gray_equalize)

showGraph(img)

cv.waitKey(0)
cv.destroyAllWindows()
#Made by Team meow meow