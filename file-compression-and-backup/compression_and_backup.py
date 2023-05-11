import os
import datetime
import zipfile

backup_path = "C:/Users/tw019032/Desktop/統合code_coverage進度2/"

backup_list = [["CasePlayer2", "C:/winAMS_CM1/", "TEST_20210111", "TEST_20210111.zip"], \
["CoverageMaster", "C:/Users/tw019032/Documents/WinAMS/", "TEST_20210111", "TEST_20210111.zip"], \
["Sources", "D:/P/20200603-TOUGOU_ECU-P06j/trunk", "Sources", "Sources.zip"], \
["Sources", "D:/P/20200603-TOUGOU_ECU-P06j/trunk", "Sources2", "Sources2.zip"]]

today = datetime.date.today()           # 取得今天的日期
os.chdir(backup_path)                   # 切換工作資料夾
date_folder = str(today) + "_時點備份"
os.mkdir(date_folder)                   # 建立日期資料夾

os.chdir(date_folder)                   # 切換工作資料夾
for i in range(3):
    os.mkdir(backup_list[i][0])         # 建立子資料夾

def compression_and_backup(folder_name, working_folder, start_dir, zip_file_name):
    os.chdir(working_folder)            # 切換工作資料夾
    with zipfile.ZipFile(backup_path + date_folder + '/' + folder_name + '/' + zip_file_name, 'w', zipfile.ZIP_DEFLATED) as zip:
        for dirpath, dirnames, filenames in os.walk(start_dir):
            for filename in filenames:
                zip.write(os.path.join(dirpath, filename))
    print("Backup successfully:", date_folder, '->', zip_file_name) # Show file moved successfully

if __name__ == '__main__':
    # 壓縮及備份資料夾(CasePlayer2)
    compression_and_backup(backup_list[0][0], backup_list[0][1], backup_list[0][2], backup_list[0][3])

    # 壓縮及備份資料夾(CoverageMaster)
    compression_and_backup(backup_list[1][0], backup_list[1][1], backup_list[1][2], backup_list[1][3])

    # 壓縮及備份資料夾(Sources)
    compression_and_backup(backup_list[2][0], backup_list[2][1], backup_list[2][2], backup_list[2][3])

    # 壓縮及備份資料夾(Sources2)
    compression_and_backup(backup_list[3][0], backup_list[3][1], backup_list[3][2], backup_list[3][3])
    os.system("pause")