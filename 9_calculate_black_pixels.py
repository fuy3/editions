import cv2
import os
import matplotlib.pyplot as plt

def calculate_black_pixels_percentage(binary_image):
    total_pixels = binary_image.shape[0] * binary_image.shape[1]
    black_pixels = total_pixels - cv2.countNonZero(binary_image)
    black_pixels_percentage = (black_pixels / total_pixels) * 100
    return black_pixels_percentage

def process_images_in_folder(input_folder):
    # 获取文件夹中的所有图片文件
    image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp'))]

    # 用于保存黑色像素占比的结果和计算平均数
    result = []
    total_black_pixels_percentage = 0

    for image_file in image_files:
        # 构建图像文件的完整路径
        image_path = os.path.join(input_folder, image_file)

        # 读取图像并转换为灰度图像
        binary_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

        # 计算黑色像素的占比
        black_pixels_percentage = calculate_black_pixels_percentage(binary_image)

        # 打印结果
        print(f"Image: {image_file}, Black pixels percentage: {black_pixels_percentage:.2f}%")

        # 将结果保存到列表中
        result.append(black_pixels_percentage)
        total_black_pixels_percentage += black_pixels_percentage

    # 计算平均数
    average_black_pixels_percentage = total_black_pixels_percentage / len(result)

    # 打印平均数
    print(f"Average black pixels percentage: {average_black_pixels_percentage:.2f}%")

    # 绘制图表
    plt.bar(image_files, result)
    plt.xlabel('Image')
    plt.ylabel('Black pixels percentage')
    plt.title('Black Pixels Percentage in Images')
    plt.xticks(rotation=45)
    plt.show()

# 指定输入文件夹路径
input_folder = 'output_chunks2/9'  # 请替换为你的文件夹路径

# 处理图像并打印结果和图表
process_images_in_folder(input_folder)
