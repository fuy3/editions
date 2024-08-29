from processing.rename import books_rename
from processing.otsu import images_binarization
from processing.remove_covers import books_remove_covers
from processing.remove_bounders import images_crop_border
from processing.chunking import images_chunking
from processing.remove_blanks import chunks_remove_blanks

input_folder = './data/orginal_data'
binary_folder = './data/binary_data'
content_folder = './data/content_data'
cropped_folder = './data/cropped_data'
chunks_folder = './data/chunks_data'
chunks_filter_folder = './data/chunks_filter_data'

"""STEP 1 原始数据重命名"""
#books_rename(input_folder)

"""STEP 2 图像二值化"""
#images_binarization(input_folder, binary_folder)

"""STEP 3 清除副文本"""
#books_remove_covers(binary_folder, content_folder)

"""STEP 4 书页边框裁切"""
#images_crop_border(content_folder, cropped_folder)

"""STEP 5 图像切块"""
#images_chunking(cropped_folder, chunks_folder , 299) #299为chunk size

"""STEP 6 移除空白图块"""
chunks_remove_blanks(chunks_folder, chunks_filter_folder)