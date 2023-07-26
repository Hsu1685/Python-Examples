# coding: utf-8
import datetime
import os
from settings import COVERAGE, CASE2, SOURCE1, SOURCE2

# 建立資料夾
def create_folder():
    now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    folder_name = "TOUGOU_backup_" + now
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)
    return folder_name


def seven_zip_dir(src, dst):
    src = [src]
    zip_command = '"C:\\Program Files\\7-Zip\\7z.exe" a -tzip -mcu {0} {1} '.format(
        dst, " ".join(src)
    )
    if os.system(zip_command) == 0:
        print("Successful backup to", dst)


if __name__ == "__main__":
    print("[備份開始]")
    new_folder = create_folder()
    print("建立備份資料夾:", new_folder)

    print("壓縮CoverageMaster資料夾中...")
    seven_zip_dir(COVERAGE, os.path.join(new_folder, "CoverageMaster.zip"))

    print("壓縮CasePlayer2資料夾中...")
    seven_zip_dir(CASE2, os.path.join(new_folder, "CasePlayer2.zip"))

    print("壓縮Sources資料夾中...")
    seven_zip_dir(SOURCE1, os.path.join(new_folder, "Sources.zip"))
    seven_zip_dir(SOURCE2, os.path.join(new_folder, "Sources2.zip"))
    print("[備份完成]")
    os.system("pause")
