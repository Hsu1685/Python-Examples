# coding: utf-8
import datetime
import os
import zipfile
from settings import COVERAGE, CASE2, SOURCE1, SOURCE2

# 建立資料夾
def create_folder():
    now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    folder_name = "TOUGOU_backup_" + now
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)
        os.mkdir(os.path.join(folder_name, "CoverageMaster"))
        os.mkdir(os.path.join(folder_name, "CasePlayer2"))
        os.mkdir(os.path.join(folder_name, "Sources"))
    return folder_name


# zipfile example
def zip_dir(src, dst):
    if not os.path.exists(src):  # 指定壓縮路徑不存在的情況下
        print("指定壓縮路徑不存在，請重新指定路徑！")  # 列印提示資訊
    else:  # 指定壓縮路徑存在的情況下
        for path, folders, files in os.walk(src):  # 遍歷指定壓縮路徑，獲得其目錄結構
            if len(os.listdir(src)) == 0:  # 指定壓縮路徑內容為空的情況下
                print("目標壓縮路徑為空，請檢查一下！")  # 列印提示資訊
            else:  # 指定壓縮路徑內容非空的情況下
                zip_file = zipfile.ZipFile(
                    os.path.join(dst, "{}.zip".format(os.path.basename(src))),
                    "w",
                    zipfile.ZIP_DEFLATED,
                )  # 建立一個.zip檔案
                new_path = path.replace(src, "")  # 將指定壓縮路徑替換為空，以得到其內部檔案和資料夾的相對路徑
                for filename in files:  # 遍歷某一層級資料夾內所有檔案
                    zip_file.write(
                        os.path.join(path, filename), os.path.join(new_path, filename)
                    )  # 向壓縮檔案內新增檔案
                for folder in folders:  # 遍歷某一層級資料夾內所有子資料夾
                    if len(os.listdir(os.path.join(path, folder))) == 0:  # 子資料夾為空的情況下
                        zip_file.write(
                            os.path.join(path, folder), os.path.join(new_path, folder)
                        )  # 向壓縮檔案內新增空資料夾
                zip_file.close()  # 對目標.zip檔案操作完畢，關閉操作物件


if __name__ == "__main__":
    new_folder = create_folder()
    print("建立備份資料夾:", new_folder)
    print("壓縮CoverageMaster資料夾中...")
    zip_dir(COVERAGE, os.path.join(new_folder, "CoverageMaster"))
    print("壓縮CasePlayer2資料夾中...")
    zip_dir(CASE2, os.path.join(new_folder, "CasePlayer2"))
    print("壓縮Sources資料夾中...")
    zip_dir(SOURCE1, os.path.join(new_folder, "Sources"))
    zip_dir(SOURCE2, os.path.join(new_folder, "Sources"))
    print("備份完成")
    os.system("pause")
