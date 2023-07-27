from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import datetime
import time

# 欲搶購的連結、登入帳號、登入密碼及其他個資
from settings import URL2, CHROME_PATH, ACC2, PWD, BuyerSSN, BirthYear, BirthMonth, BirthDay, multi_CVV2Num2

### 登入帳戶 ###
def login():
    # 透過購物車打開登入畫面
    browser.get("https://ecssl.pchome.com.tw/sys/cflow/fsindex/BigCar/BIGCAR/ItemList")
    WebDriverWait(browser, 30).until(
        expected_conditions.presence_of_element_located((By.ID, 'loginAcc'))
    )
    print("打開登入畫面")
    while True:
        # 填入登入資訊
        elem = browser.find_element_by_id('loginAcc')
        elem.clear()
        elem.send_keys(ACC2)
        print("輸入帳號")
        elem = browser.find_element_by_id('loginPwd')
        elem.clear()
        elem.send_keys(PWD)
        print("輸入密碼")
        WebDriverWait(browser, 20).until(
                expected_conditions.element_to_be_clickable((By.ID, "btnLogin"))
        )
        # 按下登入
        time.sleep(0.5)
        browser.find_element_by_id('btnLogin').click()
        print("按下登入按鈕")
        # 確認登入成功
        WebDriverWait(browser, 40).until(
            expected_conditions.title_contains(u"購物車")
        )
        if expected_conditions.title_contains(u"購物車")(browser):
            print("登入成功")
            break
        #time.sleep(1)

### 開新分頁 ###
def newTab():
    # function2:open new page with javascropt command #function2: 使用javascript指令在同一個網頁視窗中開啟新分頁
    print('開新分頁')
    url1 = 'https://ecssl.pchome.com.tw/sys/cflow/fsindex/BigCar/BIGCAR/ItemList' #step1:setup url1 you want to visit in new page
    strScript = 'window.open("'+url1+'");'
    browser.execute_script(strScript)

### 放入購物車 ###
def pickItem(times):
    # 打開購物頁面
    browser.switch_to.window(windows[0])
    browser.get(URL2)
    print("打開購物頁面，等待至預購時間......")
    while True:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        # 對比時間至開放時間前2秒
        if now > times:
            while True:
                try:
                    # 開啟網頁確認是否可以購買
                    browser.get(URL2)
                    print("購物前重新打開網頁")
                    WebDriverWait(browser, 0.3).until(
                        expected_conditions.element_to_be_clickable(
                            (By.XPATH, "//li[@id='ButtonContainer']/button"))
                    )
                    # 可購買後點擊加到購物車
                    print("確認可否購買?")
                    #print(expected_conditions.text_to_be_present_in_element(
                        #(By.XPATH, "//li[@id='ButtonContainer']/button"), "售完，補貨中！")(browser))
                    if not expected_conditions.text_to_be_present_in_element(\
                        (By.XPATH, "//li[@id='ButtonContainer']/button"), "尚未開賣！")(browser):
                        browser.find_element_by_xpath("//li[@id='ButtonContainer']/button").click()
                        print("加入購物車")
                        browser.switch_to.window(windows[1])
                        browser.refresh()
                        break
                    else:
                        print("還無法購買")
                except Exception as e:
                    print(e)
            break

### 結帳 ###
def buy():

    try:
        ### 前往購物車結帳 ###
        #browser.get("https://ecssl.pchome.com.tw/sys/cflow/fsindex/BigCar/BIGCAR/ItemList")
        print("加入購物車成功，前往購物車")
        #cardCheck()    # 信用卡結帳流程
        atmCheck()    # ATM結帳流程
    except Exception as e:
        print(e)

def atmCheck():
    ### 前往結帳 (ATM轉帳) ### (要使用 JS 的方式 execute_script 點擊)
    WebDriverWait(browser, 20).until(
        expected_conditions.element_to_be_clickable(
            (By.XPATH, "//li[@class='ATM']/a[@class='ui-btn']"))
    )
    button = browser.find_element_by_xpath(
        "//li[@class='ATM']/a[@class='ui-btn']")
    browser.execute_script("arguments[0].click();", button)
    print("結帳 (ATM轉帳)")

    ### 按下繼續 (option)###
    while(True):
        try:
            button = browser.find_element_by_xpath(
                "//a[@id='warning_btn_confirm']")
            browser.execute_script("arguments[0].click();", button)            
            print("按下繼續按鈕(1)")
            break
        except:
            print("無法按下繼續按鈕(1)")
        try:
            button = browser.find_element_by_xpath(
                "//a[@id='warning-timelimit_btn_confirm']")
            browser.execute_script("arguments[0].click();", button)
            print("按下繼續按鈕(2)")
            break
        except:
            print("無法按下繼續按鈕(2)")

    '''
    ### 按下繼續 (option)###
    WebDriverWait(browser, 20).until(
        expected_conditions.element_to_be_clickable(
            (By.XPATH, "//a[@id='warning_btn_confirm']"))
    )
    button = browser.find_element_by_xpath(
        "//a[@id='warning_btn_confirm']")
    browser.execute_script("arguments[0].click();", button)
    print("按下繼續按鈕")
    '''
    '''
    ### 按下繼續 (option)###        
    WebDriverWait(browser, 20).until(
        expected_conditions.element_to_be_clickable(
            (By.XPATH, "//a[@id='warning-timelimit_btn_confirm']"))
    )
    button = browser.find_element_by_xpath(
        "//a[@id='warning-timelimit_btn_confirm']")
    browser.execute_script("arguments[0].click();", button)
    print("按下繼續按鈕")
    '''    
    '''
    ### 填入各項資料 ### (BuyerSSN, BirthYear, BirthMonth, BirthDay, multi_CVV2Num)
    WebDriverWait(browser, 20).until(
        expected_conditions.element_to_be_clickable(
            (By.XPATH, "//input[@name='multi_CVV2Num']"))
    )
    elem = browser.find_element_by_xpath("//input[@name='multi_CVV2Num']")
    elem.send_keys(multi_CVV2Num)
    print("填入信用卡資料:CVC2")
    '''
    ### 勾選同意 ###
    WebDriverWait(browser, 20).until(
        expected_conditions.element_to_be_clickable(
            (By.XPATH, "//input[@name='chk_agree']"))
    )
    browser.find_element_by_xpath("//input[@name='chk_agree']").click()

    ### 送出訂單 ### (要使用 JS 的方式 execute_script 點擊)
    WebDriverWait(browser, 20).until(
        expected_conditions.element_to_be_clickable(
            (By.XPATH, "//a[@id='btnSubmit']"))
    )
    button = browser.find_element_by_xpath("//a[@id='btnSubmit']")
    browser.execute_script("arguments[0].click();", button)
    print("送出訂單")

def cardCheck():
    ### 前往結帳 (一次付清) ### (要使用 JS 的方式 execute_script 點擊)
    WebDriverWait(browser, 20).until(
        expected_conditions.element_to_be_clickable(
            (By.XPATH, "//li[@class='CC']/a[@class='ui-btn']"))
    )
    button = browser.find_element_by_xpath(
        "//li[@class='CC']/a[@class='ui-btn']")
    browser.execute_script("arguments[0].click();", button)
    print("結帳 (一次付清)")

    ### 按下繼續 (option)###
    WebDriverWait(browser, 20).until(
        expected_conditions.element_to_be_clickable(
            (By.XPATH, "//a[@id='warning-timelimit_btn_confirm']"))
    )
    button = browser.find_element_by_xpath(
        "//a[@id='warning-timelimit_btn_confirm']")
    browser.execute_script("arguments[0].click();", button)
    print("按下繼續按鈕")
    
    ### 填入各項資料 ### (BuyerSSN, BirthYear, BirthMonth, BirthDay, multi_CVV2Num)
    WebDriverWait(browser, 20).until(
        expected_conditions.element_to_be_clickable(
            (By.XPATH, "//input[@name='multi_CVV2Num']"))
    )
    elem = browser.find_element_by_xpath("//input[@name='multi_CVV2Num']")
    elem.send_keys(multi_CVV2Num2)
    print("填入信用卡資料")

    elem = browser.find_element_by_xpath("//input[@name='BuyerSSN']")
    elem.send_keys(BuyerSSN)
    elem = browser.find_element_by_xpath("//input[@name='BirthYear']")
    elem.send_keys(BirthYear)
    elem = browser.find_element_by_xpath("//input[@name='BirthMonth']")
    elem.send_keys(BirthMonth)
    elem = browser.find_element_by_xpath("//input[@name='BirthDay']")
    elem.send_keys(BirthDay)
    print("填入個人資料")

    ### 勾選同意 ###
    WebDriverWait(browser, 20).until(
        expected_conditions.element_to_be_clickable(
            (By.XPATH, "//input[@name='chk_agree']"))
    )
    browser.find_element_by_xpath("//input[@name='chk_agree']").click()

    ### 送出訂單 ### (要使用 JS 的方式 execute_script 點擊)
    WebDriverWait(browser, 20).until(
        expected_conditions.element_to_be_clickable(
            (By.XPATH, "//a[@id='btnSubmit']"))
    )
    button = browser.find_element_by_xpath("//a[@id='btnSubmit']")
    browser.execute_script("arguments[0].click();", button)
    print("送出訂單")

if __name__ == "__main__":
    # 指定購買時間前2秒，時間格式："2021-06-18 11:59:58.000"
    times = "2021-09-10 11:59:59.000"

    # 打開Chrome瀏覽器(Windows)
    browser = webdriver.Chrome()
    # 打開Chrome瀏覽器(Linux)
    #browser = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
    # 設計瀏覽器最大話提示
    browser.maximize_window()  

    # 登入帳號
    login()
    # 開分頁
    newTab()
    windows = browser.window_handles  #get all windows in your browser
    # 放入購物車
    pickItem(times)
    # 結帳
    buy()
