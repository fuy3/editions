import os
import shutil

def move_images(image_paths, source_folder, destination_folder):
    # 创建目标文件夹（如果不存在）
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # 遍历指定文件夹中的所有文件
    for filename in os.listdir(source_folder):
        source_path = os.path.join(source_folder, filename)
        # 只处理图像文件
        if os.path.isfile(source_path) and any(image_path in filename for image_path in image_paths):
            destination_path = os.path.join(destination_folder, filename)
            # 移动图像文件到目标文件夹
            shutil.move(source_path, destination_path)
            print(f"Moved {filename} to {destination_path}")

# 示例用法
image_paths = ['003.png', '004.png', '010.png', '014.png', '015.png', '021.png', '023.png', '029.png', '030.png', '039.png', '040.png', '059.png', '063.png', '064.png', '069.png', '070.png', '071.png', '072.png', '073.png', '074.png', '075.png', '076.png', '077.png', '078.png', '085.png', '087.png', '088.png', '089.png', '092.png', '093.png', '094.png', '095.png', '096.png', '100.png', '101.png', '102.png', '115.png', '128.png', '130.png', '131.png', '143.png', '151.png', '156.png', '157.png', '163.png', '170.png', '175.png', '179.png', '180.png', '182.png', '183.png', '186.png', '187.png', '188.png', '189.png', '190.png', '191.png', '192.png', '193.png', '194.png', '195.png', '196.png', '199.png', '204.png', '205.png', '214.png', '216.png', '218.png', '220.png', '221.png', '223.png', '227.png', '229.png', '230.png', '233.png', '235.png', '237.png', '238.png', '241.png', '243.png', '244.png', '246.png', '247.png', '249.png', '251.png', '253.png', '257.png', '260.png', '261.png', '262.png', '263.png', '265.png', '267.png', '268.png', '270.png', '275.png', '276.png', '278.png', '280.png', '282.png', '284.png', '291.png', '292.png', '293.png', '295.png', '298.png', '305.png', '309.png', '312.png', '313.png', '317.png', '319.png', '320.png', '321.png', '324.png', '325.png', '326.png', '329.png', '333.png', '338.png', '342.png', '344.png', '346.png', '347.png', '349.png', '352.png', '353.png', '354.png', '355.png', '356.png', '359.png', '360.png', '361.png', '362.png', '363.png', '367.png', '368.png', '370.png', '371.png', '372.png', '373.png', '375.png', '376.png', '378.png', '380.png', '381.png', '382.png', '383.png', '384.png', '385.png', '386.png', '387.png', '389.png', '390.png', '391.png', '393.png', '394.png', '395.png', '398.png', '399.png', '400.png', '401.png', '402.png', '403.png', '404.png', '406.png', '407.png', '410.png', '412.png', '414.png', '418.png', '419.png', '421.png', '425.png', '426.png', '428.png', '432.png', '436.png', '437.png', '438.png', '440.png', '441.png', '442.png', '445.png', '448.png', '449.png', '451.png', '452.png', '453.png', '456.png', '460.png', '461.png', '462.png', '463.png', '466.png', '468.png', '469.png', '472.png', '474.png', '478.png', '482.png', '483.png', '484.png', '486.png', '488.png', '489.png', '490.png', '499.png', '501.png', '506.png', '509.png', '545.png', '551.png', '558.png', '563.png', '564.png', '574.png', '595.png', '599.png', '601.png', '608.png', '609.png', '610.png', '611.png', '614.png', '616.png', '617.png', '618.png', '633.png', '644.png', '645.png', '665.png', '669.png', '671.png', '672.png']


# 图像路径信息
source_folder = "03_dataset_cleaned/1000000000"  # 源文件夹
destination_folder = "yesC01"  # 目标文件夹

move_images(image_paths, source_folder, destination_folder)


