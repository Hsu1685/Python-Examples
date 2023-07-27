import serial   # 引用pySerial模組
import json     # 引入json模块

COM_PORT = 'COM63'    # 指定通訊埠名稱
BAUD_RATES = 19200    # 設定傳輸速率
ser = serial.Serial(COM_PORT, BAUD_RATES)   # 初始化序列通訊埠

try:
    while True:
        while ser.in_waiting:                           # 若收到序列資料…
            data_raw = ser.readline()                   # 讀取一行
            print('接收到的原始資料：', data_raw)
            #print(type(data_raw[0]))
            if data_raw[0] == 123 and data_raw[1] ==34: # 確認原始資料必須要是' {" '開頭才是傳輸正確
                data = data_raw.decode()                # 用預設的UTF-8解碼
                print('接收到的資料：', data)
                try:
                    jsonData = json.loads(data)
                except ValueError as e:
                    print("Error:", e)
                    continue
                print("轉碼成功, 資料type為->", type(jsonData))
                print("轉碼成功, 資料firstName為->", jsonData["firstName"])
                print("轉碼成功, 資料lastName為->", jsonData["lastName"])
                print("轉碼成功, 資料age為->", jsonData["age"])

except KeyboardInterrupt:   # Ctrl + c 離開
    ser.close()             # 清除序列通訊物件
    print('再見！')