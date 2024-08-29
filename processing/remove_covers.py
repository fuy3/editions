import cv2
import os
from loguru import logger

def calculate_black_pixels_percentage(binary_image):
    """计算图像内黑色像素占比"""
    if binary_image is None:
        return None

    total_pixels = binary_image.shape[0] * binary_image.shape[1]
    black_pixels = total_pixels - cv2.countNonZero(binary_image)
    black_pixels_percentage = (black_pixels / total_pixels) * 100
    return black_pixels_percentage

def books_remove_covers(input_folder, output_folder):
    """移除书籍中的副文本页面，将正文图像另存为新文件夹"""
    os.makedirs(output_folder, exist_ok=True)

    for root, _, files in os.walk(input_folder):
        logger.debug(f"Processing folder: {root}")

        folder_result = []
        total_black_pixels_percentage = 0
        
        for image_file in files:
            if image_file.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp')):
                image_path = os.path.join(root, image_file)

                binary_image = cv2.imread(image_path, 0)

                if binary_image is not None:
                    _, binary_image = cv2.threshold(binary_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

                    black_pixels_percentage = calculate_black_pixels_percentage(binary_image)

                    if black_pixels_percentage is not None and 15.0 < black_pixels_percentage < 25.0:
                        logger.debug(f"图像：{image_file}，黑色像素占比: {black_pixels_percentage:.2f}%")

                        relative_path = os.path.relpath(root, input_folder)
                        new_image_folder = os.path.join(output_folder, relative_path)
                        os.makedirs(new_image_folder, exist_ok=True)
                        new_image_path = os.path.join(new_image_folder, image_file)
                        cv2.imwrite(new_image_path, binary_image)

                        folder_result.append(black_pixels_percentage)
                        total_black_pixels_percentage += black_pixels_percentage
                    else:
                        logger.debug(f"图像：{image_file}, 黑色像素占比: {black_pixels_percentage:.2f}% - 跳过图片")
                else:
                    logger.debug(f"读区图像 {image_file} 失败")

        if folder_result:
            average_black_pixels_percentage = total_black_pixels_percentage / len(folder_result)
            logger.debug(f"文件夹 {root} 平均黑色像素占比 {average_black_pixels_percentage:.2f}%")
        else:
            logger.debug(f"路径 {root} 下未查找到图像文件")