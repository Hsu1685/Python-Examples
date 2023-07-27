import serial   # 引用pySerial模組
import struct   # 轉換二進位
import copy     # copy串列

DEBUG = False

COM_PORT = 'COM63'    # 指定通訊埠名稱
BAUD_RATES = 19200    # 設定傳輸速率
ser = serial.Serial(COM_PORT, BAUD_RATES)   # 初始化序列通訊埠

rx_step = rx_cmd = rx_length = data_counter = 0
data_buffer_list = [0 for i in range(40)]
data_list = [[0 for i in range(40)] for j in range(10)]

# RX START Signal Check
def rx_step_0(byte):
    if byte == 214:
        if DEBUG: print('rx_step 0...')
        return 1
    else:
        return False
def rx_step_1(byte):
    if byte == 228:
        if DEBUG: print('rx_step 1...')
        return 2
    else:
        return False
def rx_step_2(byte):
    if byte == 110:
        if DEBUG: print('rx_step 2...')
        return 3
    else:
        return False
# ID of RX Signal
def rx_step_3(byte):
    if byte == 2:
        rx_id = byte
        data_buffer_list[0] = rx_id
        if DEBUG: print('rx_step 3...')
        return 4
    else:
        return False
# CMD of I2C RX Signal
def rx_step_4(byte):
    # 取得全域變數來使用
    global rx_cmd
    if ( 0 <= byte <= 20):
        rx_cmd = byte
        data_buffer_list[1] = rx_cmd
        if DEBUG: print('rx_step 4...')
        return 5
    else:
        return False
# LEN of I2C RX Signal
def rx_step_5(byte):
    global data_counter, rx_length
    if ( 0 <= byte <= 40):
        rx_length = byte
        data_buffer_list[2] = rx_length
        data_counter = 0
        if DEBUG: print('rx_step 5...')
        return 6
    else:
        return False
# DATA of I2C RX Signal
def rx_step_6(byte):
    global data_counter, rx_length
    if data_counter < rx_length:
        data_buffer_list[data_counter + 3] = byte
        data_counter += 1
        if DEBUG: print('rx_step 6...')
        if data_counter == rx_length:
            return 7
        return 6
    else:
        return False
# CHECKSUM of I2C RX Signal
def rx_step_7(byte):
    global rx_length, rx_cmd
    if DEBUG: print('rx_step 7...')
    checksum_calculation = 0
    checksum_receive = byte
    data_buffer_list[rx_length + 3] = checksum_receive
    # CHECKSUM= ID + CMD + Len + Data(x...)
    for i in data_buffer_list[0:rx_length + 3]:
        checksum_calculation = checksum_calculation + i
        if checksum_calculation > 255:
            checksum_calculation = checksum_calculation - 256        

    if checksum_calculation == checksum_receive:
        data_list[rx_cmd] = copy.deepcopy(data_buffer_list)
        if DEBUG: print('Checksum OK!')
    else:            
        print('Checksum Error!', 'received:', checksum_receive, 'calculation:', checksum_calculation) # For debug
    return 0

step_func = { 0: rx_step_0, 1: rx_step_1, 2: rx_step_2, \
        3: rx_step_3, 4: rx_step_4, 5: rx_step_5, 6: rx_step_6, 7: rx_step_7}

def data_receive(byte):
    global rx_step
    rx_step = step_func[rx_step](byte)


'''
# 測試用程式
data_receive(214)
data_receive(228)
data_receive(110)

data_receive(2)
data_receive(7)
data_receive(4)

data_receive(83)
data_receive(225)
data_receive(173)
data_receive(68)

data_receive(50)

print(data_list)
'''

if __name__ == '__main__':
    try:
        while True:
            while ser.in_waiting:  # 若收到序列資料…
                data_raw = ser.read()  # 讀取
                value = struct.unpack('>B', data_raw)[0]  # 轉換二進位的資料
                # data = data_raw.decode()  # 用預設的UTF-8解碼
                # print('接收到的原始資料：', data_raw)
                # print('轉換後的資料：', value)
                data_receive(value)  # 將資料保存於串列中
                '''
                print(data_list[7])  # 顯示CMD=7的資料
                print('CMD=7 DATA1：', data_list[7][3])  # 顯示CMD=7的第一筆資料
                '''
    except KeyboardInterrupt: # Ctrl+C 離開
        ser.close()    # 清除序列通訊物件
        print('再見！')