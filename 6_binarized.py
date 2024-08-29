import os
import cv2

def binarize_images_in_folder(input_folder, output_folder):
    # 创建保存二值化图像的文件夹
    os.makedirs(output_folder, exist_ok=True)

    # 获取文件夹中的所有文件
    file_list = os.listdir(input_folder)

    # 用于递增文件名的计数器
    counter = 1

    for file_name in file_list:
        # 检查文件是否为图像文件
        if file_name.endswith(('.jpg', '.jpeg', '.png', '.bmp')):
            # 构建图像文件的完整路径
            image_path = os.path.join(input_folder, file_name)

            # 读取图像
            image = cv2.imread(image_path, 0)  # 以灰度图像的形式读取

            # 进行二值化处理
            _, binary_image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
            otsu_threshold = _

            # 打印阈值数值
            print("Otsu Threshold:", otsu_threshold)

            # 构建保存二值化图像的文件路径
            binary_image_name = f"{counter}.png"
            binary_image_path = os.path.join(output_folder, binary_image_name)

            # 保存二值化图像
            cv2.imwrite(binary_image_path, binary_image)

            print(f"Binary image saved at: {binary_image_path}")

            # 递增计数器
            counter += 1

# 指定输入文件夹路径和输出文件夹路径
input_folder = '111/'
output_folder = './'

# 调用函数进行二值化处理并保存到新文件夹
binarize_images_in_folder(input_folder, output_folder)

