import serial   # 引用pySerial模組
import struct   # 轉換二進位
import copy     # copy串列
import json     # 引入json模块
import os
from time import sleep

DEBUG = False

COM_PORT = 'COM63'    # 指定通訊埠名稱
BAUD_RATES = 19200    # 設定傳輸速率
TIMEOUT = 0.5
ser = serial.Serial(COM_PORT, BAUD_RATES, timeout=TIMEOUT)   # 初始化序列通訊埠


if __name__ == '__main__':
    try:
        while True:
            ser.write(str.encode("ON"))  # 訊息必須是位元組類型
            #ser.write(b'ON\n')  # 訊息必須是位元組類型
            while False:  # 若收到序列資料…
                continue
            # serial.write([0x01, 0x04, 0x01])
            # 读取接收到的数据的第一行
            strData = ser.readline()
            strJson = str(strData, encoding='utf-8')
            # 把拿到的数据转为字符串(串口接收到的数据为bytes字符串类型,需要转码字符串类型)
            #strJson = str(strData, encoding='unicode_escape')
            # 如果有数据,则进行json转换
            print("Process %s says: " % os.getpid())
            print("当前接受到的数据位->", strJson)
            # 字符串转为json(每个字符串变量名必须为双引号包括,而不是单引号)
            jsonData = json.loads(strJson)
            print("转码成功,当前类型为->", type(jsonData))

    except KeyboardInterrupt: # Ctrl+C 離開
        ser.close()    # 清除序列通訊物件
        print('再見！')

'''
if __name__ == '__main__':
    try:
        while True:
             while ser.in_waiting:  # 若收到序列資料…
                # 读取接收到的数据的第一行
                strData = ser.readline()
                strJson = str(strData, encoding='utf-8')
                # 把拿到的数据转为字符串(串口接收到的数据为bytes字符串类型,需要转码字符串类型)
                #strJson = str(strData, encoding='unicode_escape')
                # 如果有数据,则进行json转换
                print("Process %s says: " % os.getpid())
                print("当前接受到的数据位->", strJson)
                # 字符串转为json(每个字符串变量名必须为双引号包括,而不是单引号)
                jsonData = json.loads(strJson)
                print("转码成功,当前类型为->", type(jsonData))

    except KeyboardInterrupt: # Ctrl+C 離開
        ser.close()    # 清除序列通訊物件
        print('再見！')'''