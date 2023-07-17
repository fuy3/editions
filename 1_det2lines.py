from PIL import Image, ImageDraw

def crop_and_save_image(input_image, coordinates):
    image = Image.open(input_image)

    x_coordinates = [int(coord[0]) for coord in coordinates]
    y_coordinates = [int(coord[1]) for coord in coordinates]

    left = min(x_coordinates)
    top = min(y_coordinates)
    right = max(x_coordinates)
    bottom = max(y_coordinates)

    cropped_image = image.crop((left, top, right, bottom))
    cropped_image.save(f"{input_image}_{nameNo}.jpg")  # 保存切割后的图像

    return cropped_image

def split(data, file_name, coordinates):
    # 查找文件名
    file_name_end = data.find(".jpg")  # 获取文件名的结束位置
    if file_name_end != -1:
        file_name_start = data.rfind(" ", 0, file_name_end) + 1  # 文件名的起始位置
        file_name.append(data[file_name_start:file_name_end + 4])  # 假设文件名以.jpg扩展名结尾

    # 查找坐标信息
    coordinatesss_start = data.find("[[[")
    if coordinatesss_start != -1:
        coordinatesss.append(data[coordinatesss_start:])# 打印结果

def read_file_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            return lines
    except FileNotFoundError:
        print(f"文件 '{file_path}' 不存在")
        return None

# 逐行读取文件内容
folder_path = "./1_dataset_lines/10/"
file_path = folder_path + "det_results.txt"  # 替换为实际的文件路径
file_lines = read_file_lines(file_path)
file_name = []
coordinatesss = []

# 打印每一行内容
if file_lines:
    for data in file_lines:
        data = data.strip()
        split(data, file_name, coordinatesss)
        #print("文件名:", file_name[0])
        #print("坐标信息:", coordinates[0])

# 示例使用
for i in range (0, len(file_name)):
    input_image = folder_path+file_name[i]  # 输入图像的文件路径
    ca = coordinatesss[i]
    #ca = ca.split(",")
    ca = eval(ca)
    print(file_name[i])

    nameNo = 1
    for i in ca:
        coordinates = i
#        print(coordinates)
        cropped_image = crop_and_save_image(input_image, coordinates)
        print (nameNo)
        nameNo += 1

