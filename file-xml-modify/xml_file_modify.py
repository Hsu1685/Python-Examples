import glob
import os
import xml.etree.ElementTree as ET

# 切換到特定工作目錄(要取得資料的檔案)
os.chdir('Read_XML')
# 尋找*.xml檔案並排序list
train_img_list = glob.glob('*.xml')
train_img_list.sort()
# 回到上層目錄
os.chdir('..')
# 切換到特定工作目錄(要被加入的檔案)
os.chdir('Write_XML')
# 尋找*.xml檔案並排序list
temp_img_list = glob.glob('*.xml')
temp_img_list.sort()
# 回到上層目錄
os.chdir('..')
# 列出檔案清單
print('[Read_XML] list: ')
print(train_img_list)
print('[Write_XML] list: ')
print(temp_img_list)

# 處理train_images中每一個xml檔
for name in train_img_list:
    # 從temp_images中間找出是否有與train_images同名的xml
    find_temp = temp_img_list.index(name)
    # 獲取 XML 文件物件 ElementTree
    tree_train = ET.parse(os.path.join('Read_XML', name))
    tree_temp = ET.parse(os.path.join('Write_XML', temp_img_list[find_temp]))
    # 獲取 XML 文件物件的根結點 Element
    root_temp = tree_temp.getroot()
    # 進入特定object節點的位置
    for obj in tree_train.findall("object"):
        # 把read的xml檔中間的object資訊貼到write的xml檔
        root_temp.append(obj)
    # 輸出檔案
    tree_temp.write(os.path.join('Output', name))
    print('Save', os.path.join('Output', name), 'done!')