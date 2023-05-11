# -*- coding: utf-8 -*-

"""This module provides the Renamer class to rename multiple files."""

import time
from pathlib import Path

from PySide6.QtCore import QObject, Signal


class Renamer(QObject):
    # Define custom signals
    progressed = Signal(int)    # 訊號用來更新進度條
    renamedFile = Signal(Path)    # 訊號用來在檔案處理後發送
    finished = Signal()    # 訊號用來在更名全部處理後發送

    def __init__(self, files, prefix, renameType):
        super().__init__()
        self._files = files    # 取得檔案清單
        self._prefix = prefix    # 取得前綴字串
        self._renameType = renameType

    def renameFiles(self):
        for fileNumber, pathlibPathClass in enumerate(self._files, 1):    # enumerate(iterable, start=0)
            newFile = self.newFileGenerator(pathlibPathClass, self._renameType, self._prefix, fileNumber, pathlibPathClass.suffix)
            pathlibPathClass.rename(newFile)    # 更名
            time.sleep(0.1)    # Comment this line to rename files faster.
            self.progressed.emit(fileNumber)    # 更名後傳送progressed訊號(訊號帶處理完的檔案編號)
            self.renamedFile.emit(newFile)    # 更名後傳送renamedFile訊號(訊號帶新檔名)
        self.progressed.emit(0)    # Reset the progress 全部完成後把進度條設為0
        self.finished.emit()    #  全部完成後後傳送finished訊號

    def newFileGenerator(self, file, renameType, prefix, fileNumber, suffix):
        if renameType == 0:
            newFile = file.parent.joinpath(    # 新檔名為"前綴+自動產生編號+副檔名"
                    f"{prefix}{str(fileNumber)}{suffix}"
            )
        elif renameType == 1:
            newFile = file.parent.joinpath(    # 新檔名為"前綴+原本檔名+副檔名"
                    f"{prefix}{str(file.stem)}{suffix}"
            )
        else:
            newFile = file.parent.joinpath(    # 新檔名為"大寫檔名+副檔名"
                    f"{str(file.stem).upper()}{suffix}"
            )
        return newFile

