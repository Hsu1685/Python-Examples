# 取得網站的下載連結
import time
import requests
from bs4 import BeautifulSoup

# 時間間隔1
search_date_1 = int(time.mktime(time.strptime("2021-09-07 00:00:00", "%Y-%m-%d %H:%M:%S")))
# 時間間隔2
search_date_2 = int(time.mktime(time.strptime("2021-09-11 00:00:00", "%Y-%m-%d %H:%M:%S")))
page = ["https://www.sehuatang.org/forum-103-1.html", "https://www.sehuatang.org/forum-103-2.html", "https://www.sehuatang.org/forum-103-3.html"]
magnet_list = []
magnet_set = set()# 建立空的集合

def find_magnet_list(path):
    r = requests.get(path) # 將網頁資料GET下來
    #print(r.text) # 印出HTML
    with open("HTMLs.txt", "w", encoding="utf-8") as w:   # Open file(Automatically clsoe):: write(If don't exist make a new one)
        for data in r.text:
            w.write(data)
            w.flush()

    soup = BeautifulSoup(r.text,"html.parser") # 將網頁資料以html.parser
    sel = soup.select("th.new a")  #取HTML標籤中的 <div class="title"></div> 中的<a>標籤存入sel
    for s in sel:
        if "thread" in s["href"]:
            url = "https://www.sehuatang.org/" + s["href"][:14] + "1-1.html"
            magnet_set.add(url)
    for u in magnet_set:
        r = requests.get(u)
        soup = BeautifulSoup(r.text,"html.parser")
        sel_time = soup.select("div.authi span") # 取HTML標中的 <div class="authi"></div> 中的<span>標籤存入sel_time
        sel_magnet = soup.select("div.blockcode ol") # 取HTML標中的 <div class="qa-header__info"></div> 中的<a>標籤存入sel            
        #print(sel_time[1]["title"]) # 印出貼文時間(%Y-%m-%d %H:%M:%S)
        publish_time = time.strptime(str(sel_time[1]["title"]), "%Y-%m-%d %H:%M:%S") # 轉成時間元組
        time_stamp = int(time.mktime(publish_time)) # 取得貼文時間(整數)
        #nowTime = int(time.time()) # 取得現在時間(整數)
        #print(time_stamp)
        if search_date_1 <= time_stamp <= search_date_2:
            for s in sel_magnet:
                print("取得", str(sel_time[1]["title"]), ":", s.text) # 找出magnet
                magnet_list.append(s.text + "\n")

if __name__ == '__main__':
    find_magnet_list(page[2])
    
    with open("URLs.txt", "w", encoding="utf-8") as w:   # Open file(Automatically clsoe):: write(If don't exist make a new one)
        for data in magnet_list:
            w.write(data)
            w.flush()