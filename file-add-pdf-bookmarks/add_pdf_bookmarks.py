# coding:utf-8
# 新增PDF書籤
# Current Working Directory: FILE_PROCESSING

from pdf_utils import MyPDFHandler, PDFHandleMode as mode
import os
import sys
#sys.reload()
#sys.setdefaultencoding('utf-8')
os.chdir("add_pdf_bookmarks")                   # 切換工作資料夾

def main():
    pdf_handler = MyPDFHandler(u'掃描檔.pdf',mode = mode.NEWLY)
    pdf_handler.add_bookmarks_by_read_txt('./bookmarks.txt',page_offset = 14)
    pdf_handler.save2file(u'掃描檔-目錄版.pdf')

if __name__ == '__main__':
    main()