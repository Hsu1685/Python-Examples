# 取得網站的下載連結(搜尋結果)
import time
import requests
from bs4 import BeautifulSoup

# 時間間隔1
search_date_1 = int(time.mktime(time.strptime("2021-06-08 00:00:00", "%Y-%m-%d %H:%M:%S")))
# 時間間隔2
search_date_2 = int(time.mktime(time.strptime("2021-06-13 00:00:00", "%Y-%m-%d %H:%M:%S")))
page = ["https://www.sehuatang.org/search.php?mod=forum&searchid=330679&orderby=lastpost&ascdesc=desc&searchsubmit=yes&kw=%E6%9C%89%E5%9D%82%E6%B7%B1%E9%9B%AA", \
    "https://www.sehuatang.org/search.php?mod=forum&searchid=330679&orderby=lastpost&ascdesc=desc&searchsubmit=yes&page=2", \
        "https://www.sehuatang.org/search.php?mod=forum&searchid=330679&orderby=lastpost&ascdesc=desc&searchsubmit=yes&page=3", \
            "https://www.sehuatang.org/search.php?mod=forum&searchid=330679&orderby=lastpost&ascdesc=desc&searchsubmit=yes&page=4", \
                "https://www.sehuatang.org/search.php?mod=forum&searchid=330679&orderby=lastpost&ascdesc=desc&searchsubmit=yes&page=5", \
                    "https://www.sehuatang.org/search.php?mod=forum&searchid=330679&orderby=lastpost&ascdesc=desc&searchsubmit=yes&page=6"]
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
    sel = soup.select("h3.xs3 a")  #取HTML標籤中的 <h3 class="xs3"></h3> 中的<a>標籤存入sel
    for s in sel:
        url = "https://www.sehuatang.org/" + s["href"]
        magnet_set.add(url)

    for u in magnet_set:
        r = requests.get(u)
        soup = BeautifulSoup(r.text,"html.parser")
        sel_magnet = soup.select("div.blockcode ol") # 取HTML標中的 <div class="blockcode"></div> 中的<ol>標籤存入sel
        for s in sel_magnet:
            magnet_list.append(s.text + "\n")

if __name__ == '__main__':
    find_magnet_list(page[1])
    
    with open("URLs.txt", "w", encoding="utf-8") as w:   # Open file(Automatically clsoe):: write(If don't exist make a new one)
        for data in magnet_list:
            w.write(data)
            w.flush()