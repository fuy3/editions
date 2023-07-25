import cv2
import os

def split_image(image, chunk_size):
    rows, cols, _ = image.shape
    chunk_list = []
    for r in range(0, rows, chunk_size):
        for c in range(0, cols, chunk_size):
            chunk = image[r:r+chunk_size, c:c+chunk_size]
            if chunk.shape[:2] == (chunk_size, chunk_size):
                chunk_list.append(chunk)
    return chunk_list

def process_and_save_images(input_folder, output_folder, chunk_size):
    for root, _, files in os.walk(input_folder):
        for image_file in files:
            if image_file.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp')):
                # 构建图像文件的完整路径
                image_path = os.path.join(root, image_file)

                # 读取图像
                image = cv2.imread(image_path)

                # 将图像切割为碎片
                chunks = split_image(image, chunk_size)

                # 获取原文件夹名作为新的保存路径一部分
                folder_name = os.path.basename(os.path.normpath(root))
                output_folder_path = os.path.join(output_folder, folder_name)
                os.makedirs(output_folder_path, exist_ok=True)

                # 保存碎片
                for i, chunk in enumerate(chunks):
                    # 获取图像文件名（不带后缀）作为碎片文件名的一部分
                    image_file_name = os.path.splitext(image_file)[0]
                    chunk_output_path = os.path.join(output_folder_path, f'{i+1}.jpg')
                    cv2.imwrite(chunk_output_path, chunk)

                    print(f"Chunk saved: {chunk_output_path}")

# 指定输入文件夹路径和输出文件夹路径
input_folder = '5_cropped_images/'  # 请替换为你的文件夹路径
output_folder = '6_output_chunks299/'  # 请替换为你想要保存碎片的文件夹路径
chunk_size = 299

# 执行批量处理和保存操作
process_and_save_images(input_folder, output_folder, chunk_size)

