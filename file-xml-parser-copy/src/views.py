# -*- coding: utf-8 -*-

"""This module provides the main window."""
import os
from pathlib import Path

from PySide6.QtCore import QThread
from PySide6.QtWidgets import QFileDialog, QWidget

from .copy import Copy
from .parse import Parse
from .ui.window import Ui_Window

FILTERS = ";;".join(
    (
        "PNG Files (*.png)",
        "JPEG Files (*.jpeg)",
        "JPG Files (*.jpg)",
        "GIF Files (*.gif)",
        "Text Files (*.txt)",
        "Python Files (*.py)",
        "MP4 Files (*.mp4)",
        "Video Files (*.mp4 *.mkv)",
    )
)

FILTER = ";;".join(("XML Files (*.xml)",))

RENAME_TYPE_MSG = (
    "image1.png, image2.png, image3.png... (prefix = 'image')",
    "new-name.txt, new-class.txt, new-number.txt... (prefix = 'new-')",
    "upper-case.png -> UPPER-CASE.png",
)


class Window(QWidget, Ui_Window):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Window()
        self.ui.setupUi(self)  # 設定UI
        self.load_xml_dir_name = ""
        self._file_count = 0
        self._file_total = 0
        # self._files = deque()    # 宣告一個deque()
        # self._files_count = len(self._files)    # 宣告一個變數是用在deque()的內部數量
        # self._updateStateWhenFilesLoadedFlag = False

        self._my_setup()  # 設定UI及目前狀態
        self._connect_signal_slot()  # 建立UI與函數的連結

    def _my_setup(self):  # __init__(self)執行: 設定目前狀態
        pass
        # self._updateStateWhenNoFiles()    # 整理UI目前的狀態
        # self._updateRenameTypeBox()

    def _connect_signal_slot(self):  # __init__(self)執行
        # 連結到load_src_button()
        self.ui.loadSrcButton.clicked.connect(self.load_src_button)
        # 連結到load_xml_button()
        self.ui.loadXmlButton.clicked.connect(self.load_xml_button)
        # 連結到renameFiles()
        self.ui.runButton.clicked.connect(self.copy_file)
        # # 連結renameFilesButton.textChanged到_updateStateWhenReady()
        # self.prefixEdit.textChanged.connect(self._updateStateWhenReady)
        # self.renameTypeBox.currentTextChanged.connect(self._updateRenameTypeBox)
        # self.renameTypeBox.currentTextChanged.connect(self._updateStateWhenReady)

    def load_src_button(self):
        # self.dstFileList.clear()
        if self.ui.dirEdit.text():
            init_dir = self.ui.dirEdit.text()  # 起始資料夾為dirEdit文字
        else:
            init_dir = str(Path.home())  # 起始資料夾選擇為Path.home()文字 (例如C:\Users\tw019032)
        folder_path = QFileDialog.getExistingDirectory(
            self, "Select folder", init_dir
        )  # start path
        # print(folder_path)
        self.ui.dirEdit.setText(folder_path)

    def load_xml_button(self):
        # self.dstFileList.clear()
        if self.ui.dirEdit_2.text():
            temp_path = self.ui.dirEdit_2.text()
            initDir = str(Path(temp_path).parent)  # 起始資料夾為dirEdit_2文字的父目錄
        else:
            initDir = str(Path.home())  # 資料夾選擇為Path.home()文字 (例如C:\Users\tw019032)
        file, filter = QFileDialog.getOpenFileNames(  # 檔案選擇窗口
            self, "Select XML file", initDir, filter=FILTER
        )
        if len(file) > 0:
            file_text = str(file[0])
            self.ui.dirEdit_2.setText(file_text)  # 顯示畫面的dirEdit文字
            # 分析XML檔產生Model List
            self._parse = Parse()
            self._parse.model_list_generate(new_xml_file=file_text)
            self.ui.comboBox.addItems(self._parse.model_list)

    def copy_file(self):
        self.ui.loadSrcButton.setEnabled(False)    # 關閉loadSrcButton
        self.ui.loadXmlButton.setEnabled(False)    # 關閉loadXmlButton
        self.ui.runButton.setEnabled(False)    # 關閉loadXmlButton
        # 分析XML檔案
        self._parse.update_model(self.ui.comboBox.currentIndex())
        self._parse.file_name_generate()
        self._file_total = len(self._parse.file_list_1)
        # 進行複製
        self._run_copy_thread()

    def _run_copy_thread(self):
        self._thread = QThread()  # 建立一個QThread()
        self._copy = Copy(# 建立一個Copy class
            self.ui.dirEdit.text(),
            os.getcwd(),
            self._parse.file_list_1,
            self._parse.file_list_2
        )
        self._copy.moveToThread(self._thread)
        """ Copy """
        self._thread.started.connect(self._copy.copy_file_progress)    # This signal is emitted from the associated thread when it starts executing, before the run() function is called.
        """ Update state """
        self._copy.progressed.connect(self._update_progress_bar)    # 連結progressed signal到_update_progress_bar()
        self._copy.finished.connect(self._get_finished_signal)    # finished signal到_get_finished_signal()
        """ Clean up """
        self._copy.finished.connect(self._thread.quit)    # finished signal到_thread.quit()
        self._copy.finished.connect(self._copy.deleteLater)    # finished signal到_copy.deleteLater()
        self._thread.finished.connect(self._thread.deleteLater)    # _thread.finished signal到_renamer._thread.deleteLater()
        """ Run the thread """
        self._thread.start()

    def _update_progress_bar(self, new_file):    # 更新進度條狀態 (處理完1個檔案後就會被progressed signal觸發1次)
        self._file_count += 1
        progressPercent = int(self._file_count / self._file_total * 100)    # 計算進度百分比
        self.ui.progressBar.setValue(progressPercent)    # 設定進度條數值
        self.ui.dstFileList.addItem(str(new_file))

    def _get_finished_signal(self):
        self.ui.loadSrcButton.setEnabled(True)    # 打開loadSrcButton
        self.ui.loadXmlButton.setEnabled(True)    # 打開loadXmlButton


















    def _updateStateWhenNoFiles(self):  # __init__(self) -> _setupUI(self)執行
        self._filesCount = len(self._files)
        self.loadFilesButton.setEnabled(True)
        self.loadFilesButton.setFocus()
        self.renameFilesButton.setEnabled(False)
        self.prefixEdit.clear()  # 前綴欄位清除
        self.prefixEdit.setEnabled(False)  # 前綴欄位不啟用

        # self.renameTypeLabel.setText(None)
        # print('run _updateStateWhenNoFiles()')

    def _connectSignalsSlots(self):  # __init__(self):執行
        self.loadFilesButton.clicked.connect(
            self.loadFiles
        )  # 連結loadFilesButton.clicked到loadFiles()
        self.renameFilesButton.clicked.connect(
            self.renameFiles
        )  # 連結renameFilesButton.clicked到renameFiles()
        self.prefixEdit.textChanged.connect(
            self._updateStateWhenReady
        )  # 連結renameFilesButton.textChanged到_updateStateWhenReady()
        self.renameTypeBox.currentTextChanged.connect(self._updateRenameTypeBox)
        self.renameTypeBox.currentTextChanged.connect(self._updateStateWhenReady)

    def _updateStateWhenReady(self):
        if self._updateStateWhenFilesLoadedFlag == True:
            if self.renameTypeBox.currentIndex() == 2:
                self.renameFilesButton.setEnabled(True)
            else:
                if self.prefixEdit.text():
                    self.renameFilesButton.setEnabled(True)
                else:
                    self.renameFilesButton.setEnabled(False)
        # print('run _updateStateWhenReady()')

    def loadFiles(self):
        self.dstFileList.clear()
        if self.dirEdit.text():
            initDir = self.dirEdit.text()  # 資料夾選擇為dirEdit文字
        else:
            initDir = str(Path.home())  # 資料夾選擇為Path.home()文字 (例如C:\Users\tw019032)
        files, filter = QFileDialog.getOpenFileNames(  # 檔案選擇窗口
            self, "Choose Files to Rename", initDir, filter=FILTERS
        )
        if len(files) > 0:
            fileExtension = filter[filter.index("*") : -1]  # 設定fileExtension字串
            self.extensionLabel.setText(fileExtension)  # 顯示畫面的extensionLabel文字
            srcDirName = str(Path(files[0]).parent)  # 設定srcDirName字串
            self.dirEdit.setText(srcDirName)  # 顯示畫面的dirEdit文字
            for file in files:  # 處理所選擇的每個檔案
                self._files.append(Path(file))  # 加入選擇的Path(file)到deque()裡
                self.srcFileList.addItem(file)  # 加入選擇的Path(file)到畫面srcFileList裡
            self._filesCount = len(
                self._files
            )  # 計算deque()裡的資料數量 (要處理的檔案總數，後面用來計算進度條百分比)
            self._updateStateWhenFilesLoaded()  # 選擇檔案後，更名前的準備

    def _updateStateWhenFilesLoaded(self):
        if not self.renameTypeBox.currentIndex() == 2:
            self.prefixEdit.setEnabled(True)  # 把前綴編輯欄位打開
            self.prefixEdit.setFocus()  # 游標放在前綴編輯欄位打開
        self._updateStateWhenFilesLoadedFlag = True

    def renameFiles(self):
        self._runRenamerThread()  # 進行更名
        self._updateStateWhileRenaming()  # 進行狀態更新

    def _updateStateWhileRenaming(self):
        self.loadFilesButton.setEnabled(False)  # 關閉loadFilesButton
        self.renameFilesButton.setEnabled(False)  # 關閉renameFilesButton
        self._updateStateWhenFilesLoadedFlag = False

    def _runRenamerThread(self):
        if self.prefixEdit.isEnabled():
            prefix = self.prefixEdit.text()  # 取得前綴
        else:
            prefix = None  # 取得前綴
        self._thread = QThread()  # 建立一個QThread()
        self._renamer = Renamer(  # 建立一個Renamer class
            files=tuple(self._files),
            prefix=prefix,
            renameType=self.renameTypeBox.currentIndex(),
        )
        self._renamer.moveToThread(self._thread)
        # Rename
        self._thread.started.connect(
            self._renamer.renameFiles
        )  # This signal is emitted from the associated thread when it starts executing, before the run() function is called.
        # Update state
        self._renamer.renamedFile.connect(
            self._updateStateWhenFileRenamed
        )  # 連結renamedFile signal到_updateStateWhenFileRenamed()
        self._renamer.progressed.connect(
            self._updateProgressBar
        )  # 連結progressed signal到_updateProgressBar()
        self._renamer.finished.connect(
            self._updateStateWhenNoFiles
        )  # finished signal到_updateStateWhenNoFiles()
        # Clean up
        self._renamer.finished.connect(
            self._thread.quit
        )  # finished signal到_thread.quit()
        self._renamer.finished.connect(
            self._renamer.deleteLater
        )  # finished signal到_renamer.deleteLater()
        self._thread.finished.connect(
            self._thread.deleteLater
        )  # _thread.finished signal到_renamer._thread.deleteLater()
        # Run the thread
        self._thread.start()

    def _updateStateWhenFileRenamed(self, newFile):  # 更新改名後的狀態 (處理完1個檔案後就會被renamedFile signal觸發1次)
        self._files.popleft()  # Remove and return an element from the left side of the deque
        self.srcFileList.takeItem(
            0
        )  # Removes and returns the item from the given row 0
        self.dstFileList.addItem(
            str(newFile)
        )  # Inserts an item with the text label at the end of the list widget

    def _updateProgressBar(
        self, fileNumber
    ):  # 更新進度條狀態 (處理完1個檔案後就會被progressed signal觸發1次)
        progressPercent = int(fileNumber / self._filesCount * 100)  # 計算進度百分比
        self.progressBar.setValue(progressPercent)  # 設定進度條數值

    def _updateRenameTypeBox(self):
        boxIndex = self.renameTypeBox.currentIndex()
        self.renameTypeLabel.setText(RENAME_TYPE_MSG[boxIndex])
        if self._updateStateWhenFilesLoadedFlag == True:
            if not boxIndex == 2:
                self.prefixEdit.setEnabled(True)  # 把前綴編輯欄位打開
                self.prefixEdit.setFocus()  # 游標放在前綴編輯欄位打開
            else:
                self.prefixEdit.setEnabled(False)  # 把前綴編輯欄位打開
