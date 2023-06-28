import cv2
import numpy as np
import os

"""
判断是否是白块
"""


def isSpace(img):
    ptSum = np.sum(img)
    """
    空白数大于阈值
    """
    if ptSum < img.size * 0.7:
        return True
    return False


"""
获得文字部分的文字
"""


def findChars(img, img_width):
    chars = []
    contours, _ = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    char_heights = []
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        aspect_ratio = w / h
        if aspect_ratio < 10 and 0.5 <= w / img_width <= 2.0:  # 考虑宽度与输入原图的宽度接近，不限制长宽比例
            char = img[y:y+h, x:x+w]
            if not isSpace(char):
                chars.append(char)
                char_heights.append(h)

    # 计算字符高度的平均值
    avg_height = np.mean(char_heights)

    # 过滤掉高度与平均值差距较大的字符
    filtered_chars = []
    for char, height in zip(chars, char_heights):
        if 0.8 <= height / avg_height <= 1.2:
            filtered_chars.append(char)

    return filtered_chars


"""
分割函数主体封装
"""


def splitImg(imgPath):
    imgName = os.path.splitext(os.path.basename(imgPath))[0]

    print(imgName + "开始分割...")

    img = cv2.imread(imgPath, cv2.IMREAD_GRAYSCALE)

    _, binary_img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)


        # 将黑白颜色恢复成原图的颜色
        char = 255 - char  # 反转黑白色调

        cv2.imwrite(os.path.join(saveFilePath, f"img{charCount}.png"), char)
        charCount += 1

    print(imgName + "分割完成!")


def process_folder(folder_path):
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path) and file_path.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
            splitImg(file_path)

if __name__ == "__main__":
    folder_path = './dataset_seged'  # 请替换为你的文件夹路径
    process_folder(folder_path)

