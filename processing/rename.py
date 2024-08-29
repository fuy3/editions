import os
import re
from loguru import logger

def books_rename(folder_path):
    """遍历指定路径下全部子文件夹，将全部图像按照数字编号重命名"""
    for root, _, files in os.walk(folder_path):
        image_files = [f for f in files if f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))]
        if not image_files:
            continue

        image_files = sorted(image_files, key=lambda x: int(re.sub('\D', '', x)))
        num_digits = len(str(len(image_files)))

        for index, file_name in enumerate(image_files):
            file_ext = os.path.splitext(file_name)[1]
            new_file_name = f"{index + 1:0{num_digits}d}{file_ext}"

            old_file_path = os.path.join(root, file_name)
            new_file_path = os.path.join(root, new_file_name)

            os.rename(old_file_path, new_file_path)
            logger.debug(f"Renamed {file_name} to {new_file_name}")




