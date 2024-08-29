import cv2
import numpy as np
import os
from loguru import logger

def calculate_column_sums(binary_image):
    """计算每列的黑色像素总和"""
    column_sums = np.sum(binary_image == 0, axis=0)
    return column_sums

def calculate_row_sums(binary_image):
    """计算每行的黑色像素总和"""
    row_sums = np.sum(binary_image == 0, axis=1)
    return row_sums

def find_highest_column_in_half(column_sums, start_col, end_col):
    """查找横边"""
    highest_index = np.argmax(column_sums[start_col:end_col])
    highest_index += start_col
    return highest_index

def find_highest_row_in_half(row_sums, start_row, end_row):
    """查找竖边"""
    highest_index = np.argmax(row_sums[start_row:end_row])
    highest_index += start_row
    return highest_index

def images_crop_border(input_folder, output_folder):
    """裁切扫描书页边框"""
    os.makedirs(output_folder, exist_ok=True)
    for root, dirs, files in os.walk(input_folder):
        image_files = [f for f in os.listdir(root) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

        for image_file in image_files:
            image_path = os.path.join(root, image_file)
            binary_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

            if binary_image is None:
                logger.debug(f"Error: 图像读区失败 {image_file}.")
            else:
                column_sums = calculate_column_sums(binary_image)
                row_sums = calculate_row_sums(binary_image)

                # 统计图像长宽
                image_width = binary_image.shape[1]
                image_height = binary_image.shape[0]

                # 查找图像中点坐标
                half_column = image_width // 2
                half_row = image_height // 2

                # 查找边框坐标
                highest_left_column = find_highest_column_in_half(column_sums, 0, half_column)
                highest_right_column = find_highest_column_in_half(column_sums, half_column, image_width)
                highest_top_row = find_highest_row_in_half(row_sums, 0, half_row)
                highest_bottom_row = find_highest_row_in_half(row_sums, half_row, image_height)

                # 图像裁切及存储
                cropped_image = binary_image[highest_top_row:highest_bottom_row, highest_left_column:highest_right_column]
                
                relative_path = os.path.relpath(root, input_folder)
                output_subfolder = os.path.join(output_folder, relative_path)
                os.makedirs(output_subfolder, exist_ok=True)

                cropped_image_path = os.path.join(output_subfolder, image_file)
                cv2.imwrite(cropped_image_path, cropped_image)

                logger.debug(f"图像处理完成，存储路径：{cropped_image_path}.")