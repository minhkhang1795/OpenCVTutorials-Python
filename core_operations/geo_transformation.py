import cv2
import numpy as np
from matplotlib import pyplot   as plt

img = cv2.imread('sudoku.jpg', 0)
rows, cols = img.shape


def shift_image():
    M = np.float32([[1, 0, 20], [0, 1, 20]])
    dst = cv2.warpAffine(img, M, (cols, rows))
    return dst


def rotate_image():
    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 45, 0.2)
    dst = cv2.warpAffine(img, M, (cols, rows))
    return dst


def affine_transform():
    pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
    pts2 = np.float32([[10, 100], [200, 50], [100, 250]])

    M = cv2.getAffineTransform(pts1, pts2)

    dst = cv2.warpAffine(img, M, (cols, rows))

    # 121 here is row 1, column 2, plot_num 1
    plt.subplot(121), plt.imshow(img), plt.title('Input')
    plt.subplot(122), plt.imshow(dst), plt.title('Output')

    plt.show()


def perspective_transform():
    pts1 = np.float32([[56, 65], [368, 52], [28, 387], [389, 390]])
    pts2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])

    M = cv2.getPerspectiveTransform(pts1, pts2)

    dst = cv2.warpPerspective(img, M, (300, 300))

    plt.subplot(121), plt.imshow(img), plt.title('Input')
    plt.subplot(122), plt.imshow(dst), plt.title('Output')
    plt.show()


perspective_transform()
# dst = rotate_image()
# cv2.imshow('img', dst)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
