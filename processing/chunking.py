import cv2
import os
from loguru import logger

def split_image(image, chunk_size):
    rows, cols, _ = image.shape
    chunk_list = []
    for r in range(0, rows, chunk_size):
        for c in range(0, cols, chunk_size):
            chunk = image[r:r+chunk_size, c:c+chunk_size]
            if chunk.shape[:2] == (chunk_size, chunk_size):
                chunk_list.append(chunk)
    return chunk_list

def images_chunking(input_folder, output_folder, chunk_size):
    """将处理后文件切块"""
    for root, _, files in os.walk(input_folder):
        for image_file in files:
            if image_file.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp')):
                image_path = os.path.join(root, image_file)
                image = cv2.imread(image_path)
                chunks = split_image(image, chunk_size)

                folder_name = os.path.basename(os.path.normpath(root))
                output_folder_path = os.path.join(output_folder, folder_name)
                os.makedirs(output_folder_path, exist_ok=True)

                for i, chunk in enumerate(chunks):
                    image_file_name = os.path.splitext(image_file)[0]
                    chunk_output_path = os.path.join(output_folder_path, f'img{image_file_name}_chunk{i+1}.jpg')
                    cv2.imwrite(chunk_output_path, chunk)

                    logger.debug(f"Chunk保存至: {chunk_output_path}")
