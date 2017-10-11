import numpy as np
import cv2
from matplotlib import pyplot as plt


def mat_plot(image):
    # Using Matplotlib
    plt.imshow(image, cmap='gray', interpolation='bicubic')
    plt.xticks([]), plt.yticks([])
    plt.show()


def display_image(image):
    # Display an image
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    cv2.imshow('image', image)
    k = cv2.waitKey(0)

    if k == 27:
        cv2.destroyAllWindows()
    elif k == ord('s'):
        cv2.imwrite('messigray.png', image)
        cv2.destroyAllWindows()


def test_func():
    # Load an color image in grayscale
    img = cv2.imread('messi5.jpg', 0)
    display_image(img)
