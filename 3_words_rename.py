import os
import re

def batch_rename_images(folder_path, new_prefix):
    # 获取文件夹中的图像文件列表
    image_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))
                   and f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))]

    # 对文件名中的数字进行提取和排序
    image_files = sorted(image_files, key=lambda x: int(re.sub('\D', '', x)))

    # 逐个重命名图像文件
    for index, file_name in enumerate(image_files):
        # 构建新的文件名
        file_ext = os.path.splitext(file_name)[1]
        new_file_name = f"{index + 1:03d}{file_ext}"
        
        # 生成新的文件路径
        old_file_path = os.path.join(folder_path, file_name)
        new_file_path = os.path.join(folder_path, new_file_name)

        # 执行重命名操作
        os.rename(old_file_path, new_file_path)
        print(f"Renamed {file_name} to {new_file_name}")

# 指定要重命名的文件夹路径和新的文件名前缀
folder_path = './output_chunks2/9'  # 请替换为你的文件夹路径
new_prefix = ''   # 请替换为你想要的新前缀

# 执行批量重命名操作
batch_rename_images(folder_path, new_prefix)

