# -*- coding: utf-8 -*-

import xml.etree.ElementTree as et

class Parse(object):

    def __init__(self):
        super().__init__()
        self._xml_file = ""  # 取得xml檔案名稱
        self._model_type = 0  # 取得機種
        self.file_list_1 = []
        self.file_list_2 = []
        self.model_list = []
        self._tree = None
        self._root = None
        # self._prefix = prefix    # 取得前綴字串
        # self._renameType = renameType

    def _update_root(self):
        self._tree = et.ElementTree(file=self._xml_file)
        self._root = self._tree.getroot()

    def model_list_generate(self, new_xml_file):  # 每次選擇xml檔案後執行
        self.model_list = []
        self._xml_file = new_xml_file  # 取得xml檔案位置
        self._update_root()
        for child in self._root[0]:
            # print(child[0].text)
            self.model_list.append(child[0].text)

    def file_name_generate(self):  # 按下執行分析按鈕後
        self.file_list_1 = []
        self.file_list_2 = []
        model_root = self._root[0][self._model_type]  # 看combo box選到哪一個機種
        for data in model_root[2]:
            path = data.find("PATH").text
            access_path = data.find("ACCESSPATH").text
            if ((path[-2:]==".c") or (path[-2:]==".h")):
                self.file_list_1.append(path)  # 找檔名
                # print(path)
                self.file_list_2.append(access_path)  # 找檔案位置
                # print(access_path)

    def update_model(self, new_model):  # 每次改變機種選擇後執行
        self._model_type = new_model  # 取得機種

if __name__ == "__main__":
    pass