import cv2
import numpy as np

def crop_white_borders(binary_image):
    # 使用闭运算来填充噪音和连接断开的边界
    kernel = np.ones((20, 20), np.uint8)
    cleaned_image = cv2.morphologyEx(binary_image, cv2.MORPH_CLOSE, kernel)

    # 获取图像的高度和宽度
    height, width = cleaned_image.shape

    # 计算上边界的位置
    top_border = 0
    while np.sum(cleaned_image[top_border]) == width * 255:
        top_border += 1

    # 计算下边界的位置
    bottom_border = height - 1
    while np.sum(cleaned_image[bottom_border]) == width * 255:
        bottom_border -= 1

    # 计算左边界的位置
    left_border = 0
    while np.sum(cleaned_image[:, left_border]) == height * 255:
        left_border += 1

    # 计算右边界的位置
    right_border = width - 1
    while np.sum(cleaned_image[:, right_border]) == height * 255:
        right_border -= 1

    # 裁剪图像
    cropped_image = cleaned_image[top_border:bottom_border+1, left_border:right_border+1]

    return cropped_image

# 读取已经二值化后的书本图像
binary_image = cv2.imread('111/1.png', cv2.IMREAD_GRAYSCALE)

# 裁剪图像
cropped_image = crop_white_borders(binary_image)

# 显示原始图像和裁剪后的图像
cv2.imshow('Original Binary Image', binary_image)
cv2.imshow('Cropped Image', cropped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()