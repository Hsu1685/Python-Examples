# -*- coding: utf-8 -*-

"""This module provides the Renamer class to rename multiple files."""

import datetime
import shutil
from pathlib import Path
from PySide6.QtCore import QObject, Signal

class Copy(QObject):
    # Define custom signals
    progressed = Signal(str)  # 訊號用來更新進度條
    finished = Signal()  # 訊號用來在更名全部處理後發送

    def __init__(self, src, dst, file_list_1, file_list_2):
        super().__init__()
        self._src = src  # 取得檔案來源位置
        self._dst = dst  # 取得新檔案位置
        self._file_list_1 = file_list_1
        self._file_list_2 = file_list_2

    def copy_file_progress(self):
        """ 建立結果資料夾 """
        now = datetime.datetime.now().strftime("_%H%M%S")
        folder_name = "Sources" + now
        if not Path(folder_name).is_dir():
            Path(folder_name).mkdir()
        """ 執行複製 """
        for list_number, file_name in enumerate(self._file_list_1):  # enumerate(iterable, start=0)
            src_path = self._src_path_generate(file_name, self._file_list_2[list_number])
            dst_path = self._dst_path_generate(file_name, folder_name)
            try:
                shutil.copy2(src_path, dst_path)
            except Exception as other:
                print("Error", other)
                file_name = "無法複製" + file_name
            self.progressed.emit(file_name)  # 更名後傳送progressed訊號(訊號帶檔名)
        self.finished.emit()  #  全部完成後後傳送finished訊號

    def _src_path_generate(self, path, access_path):
        return str(Path('/').joinpath(Path(self._src).parent, access_path, path))

    def _dst_path_generate(self, file, folder):
        return str(Path('/').joinpath(self._dst, folder, file))

if __name__ == "__main__":
    """ 單檔測試用 """
    source = Path('/').joinpath(Path.cwd(), "ref", "Sources")
    destination = Path.cwd()
    list_1 = ["abc.c", "def.c"]
    list_2 = ["Sources", "Sources\def"]
    copy_test = Copy(source, destination, list_1, list_2)
    copy_test.copy_file_progress()
