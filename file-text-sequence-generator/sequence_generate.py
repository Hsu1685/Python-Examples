read_file = open("read1.txt", "r", encoding="utf-8")    # 開啟檔案: 唯讀(encoding="utf-8"對應檔案的中文等字型)
write_file = open("write.txt", "w", encoding="utf-8")    # 開啟檔案: 寫入(如果沒有就新建)

for lines in read_file.readlines():    # 重複執行lines = read_file.readlines()
    a1 = lines.find("{")    # 找到"{"位置
    a2 = lines.find(", ")    # 找到", "位置
    event = lines[a1+1:a2]    # 擷取字串片段
    print(event, end='')    # 印出來event
    print(" ", end='')    # end=''避免換行

    a3 = lines.find(", ", a2)
    a4 = lines.find(", ", a3+1)
    current_state = lines[a3+2:a4]
    print(current_state, end='')    # 印出來current_state
    print(" ", end='')

    a5 = lines.find(", ", a4)
    a6 = lines.find(", ", a5+1)
    func = lines[a5+2:a6]
    print(func, end='')    # 印出來func
    print(" ", end='')

    a7 = lines.find(", ", a6)
    a8 = lines.find("}")
    next_state = lines[a7+2:a8]
    print(next_state)    # 印出來next_state

    # s1 = "Note left of RX_STEP_0: rx_step_1_func"
    s1 = "Note left of %s: %s\n"
    write_file.write(s1%(current_state, func))    # 依格式寫入第一句至檔案
    # s2 = "RX_STEP_0->RX_STEP_1 : EVENT_1"
    s2 = "%s->%s : %s"
    write_file.write(s2%(current_state, next_state, event))    # 依格式寫入第二句至檔案
    write_file.write("\n")    # 寫入換行
read_file.close()    # 關閉讀取的檔案
write_file.close()    # 關閉寫入的檔案