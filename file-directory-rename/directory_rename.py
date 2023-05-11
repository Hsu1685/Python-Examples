import os, sys

path = os.getcwd() + "\directory_rename\\Test_Folder"   # 取得路徑
dirs = os.listdir(path)                                 # 取得路徑中的檔名
os.chdir("directory_rename\\Test_Folder")               # 切換工作資料夾

for dir in dirs:
    p1 = dir.find('_')                  # 找到第一個"_"位置
    s1 = dir[:p1]                       # 取得"_"前半段
    s2 = dir[p1+1:]                     # 取得"_"的後半段
    new_name = s2 + '_' + s1            # 產生新的檔名
    os.rename(str(dir),str(new_name))   #修改檔名
    print ("重新命名成功:", dir, "->",  new_name, '!')   # 顯示訊息

# 印出重新命名後的目錄
print ("新目錄為: %s" %os.listdir(os.getcwd()))