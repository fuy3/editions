import re

# 定义保存坐标的列表
coordinates = []

# 读取txt文件
with open('/Users/yimingfu/Desktop/test111/input.txt', 'r') as file:
    # 逐行读取文件内容
    for line in file:
        # 使用正则表达式提取坐标
        print(line)
        for a in line:
        matches = re.findall(r'\[\[([^]]+)\]\]', line)
        if matches:
            # 将匹配到的坐标添加到列表中
            coordinates.extend(matches)

# 打印提取到的坐标
for coordinate in coordinates:
    print(coordinate)
print("111")

