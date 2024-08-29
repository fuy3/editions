import cv2
import os
from loguru import logger


def images_binarization(input_folder, output_folder):
    """遍历指定路径下全部子文件夹，将全部图像使用Otsu方法进行二值化处理"""
    os.makedirs(output_folder, exist_ok=True)

    for root, dirs, files in os.walk(input_folder):
        for file_name in files:
            if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                image_path = os.path.join(root, file_name)
                image = cv2.imread(image_path, 0)

                if image is not None:
                    _, binary_image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
                    otsu_threshold = _

                    relative_path = os.path.relpath(root, input_folder)
                    output_subfolder = os.path.join(output_folder, relative_path)
                    os.makedirs(output_subfolder, exist_ok=True)

                    binary_image_path = os.path.join(output_subfolder, file_name)
                    cv2.imwrite(binary_image_path, binary_image)

                    logger.debug(f"Otsu二值化阈值: {otsu_threshold}, 图像保存至 {binary_image_path}")
                else:
                    logger.debug(f"图像读区失败， 路径: {image_path}")