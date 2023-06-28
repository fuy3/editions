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
    cropped_image.save(f"10_06_{nameNo}.jpg")  # 保存切割后的图像

    return cropped_image

# 示例使用
input_image = "10_6.jpg"  # 输入图像的文件路径

ca = [[[700.0, 419.0], [771.0, 418.0], [774.0, 744.0], [703.0, 744.0]], [[472.0, 209.0], [555.0, 207.0], [559.0, 362.0], [476.0, 364.0]], [[142.0, 208.0], [214.0, 208.0], [211.0, 1297.0], [138.0, 1297.0]], [[588.0, 205.0], [666.0, 205.0], [663.0, 1385.0], [585.0, 1385.0]], [[248.0, 206.0], [321.0, 206.0], [326.0, 1376.0], [252.0, 1376.0]], [[365.0, 205.0], [439.0, 205.0], [434.0, 1355.0], [360.0, 1355.0]], [[811.0, 205.0], [885.0, 205.0], [885.0, 359.0], [811.0, 359.0]], [[26.0, 200.0], [95.0, 200.0], [100.0, 1193.0], [31.0, 1193.0]], [[926.0, 192.0], [994.0, 192.0], [994.0, 665.0], [926.0, 665.0]]]


nameNo = 1
for i in ca:
    #coordinates = [[2195.0, 285.0], [2288.0, 286.0], [2270.0, 1375.0], [2177.0, 1374.0]]  # 坐标点信息

    coordinates = i
    cropped_image = crop_and_save_image(input_image, coordinates)
    print (nameNo)
    nameNo += 1

