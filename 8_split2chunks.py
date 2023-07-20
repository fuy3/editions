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
    # 创建保存碎片的文件夹
    os.makedirs(output_folder, exist_ok=True)

    # 获取文件夹中的所有图片文件
    image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp'))]

    for image_file in image_files:
        # 构建图像文件的完整路径
        image_path = os.path.join(input_folder, image_file)

        # 读取图像
        image = cv2.imread(image_path)

        # 将图像切割为碎片
        chunks = split_image(image, chunk_size)

        # 保存碎片
        for i, chunk in enumerate(chunks):
            chunk_output_path = os.path.join(output_folder, f'{os.path.splitext(image_file)[0]}_chunk_{i}.jpg')
            cv2.imwrite(chunk_output_path, chunk)

            print(f"Chunk saved: {chunk_output_path}")

# 指定输入文件夹路径和输出文件夹路径
input_folder = 'dataset/cropped_images/9/'  # 请替换为你的文件夹路径
output_folder = 'output_chunks2/9'  # 请替换为你想要保存碎片的文件夹路径
chunk_size = 448

# 执行批量处理和保存操作
process_and_save_images(input_folder, output_folder, chunk_size)
