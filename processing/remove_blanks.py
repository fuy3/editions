import cv2
import os
from loguru import logger

def calculate_black_pixels_percentage(binary_image):
    """统计界面黑色像素占比"""
    total_pixels = binary_image.shape[0] * binary_image.shape[1]
    black_pixels = total_pixels - cv2.countNonZero(binary_image)
    black_pixels_percentage = (black_pixels / total_pixels) * 100
    return black_pixels_percentage

def chunks_remove_blanks(input_folder, output_folder):
    """移除空白chunks"""
    for root, _, files in os.walk(input_folder):
        for image_file in files:
            if image_file.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp')):
                image_path = os.path.join(root, image_file)
                binary_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)


                black_pixels_percentage = calculate_black_pixels_percentage(binary_image)

                # 判断黑色像素占比是否低于8%，跳过不符合条件的图像
                if black_pixels_percentage < 8.0:
                    logger.debug(f"Chunk: {image_path} 黑色像素占比: {black_pixels_percentage:.2f}% - 跳过chunk.")
                    continue

                output_subfolder = os.path.relpath(root, input_folder)
                output_subfolder_path = os.path.join(output_folder, output_subfolder)
                os.makedirs(output_subfolder_path, exist_ok=True)
                output_image_path = os.path.join(output_subfolder_path, image_file)
                cv2.imwrite(output_image_path, cv2.imread(image_path))
                logger.debug(f"Chunk: {image_path} 黑色像素占比: {black_pixels_percentage:.2f}%")
