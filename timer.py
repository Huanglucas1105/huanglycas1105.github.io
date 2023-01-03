#初始化套件
import time
import os

#變數初始化
timer = 0
is_break = False

#定義(A) --> 清除畫面(windows)
def clearconswin():
    os.system('cls')

#定義(B) --> 設定時間
def settime():
    global timer, is_break
    try:
        timer = int(input("輸入時間... "))
        if timer == 0:
            print('離開...')
            is_break = True
    except ValueError:
        print('再嘗試一次...')
        clearconswin()
        retry()

#定義(C) --> 重設
def retry():
    settime()

#迴圈
while True:
    clearconswin()
    settime()
    if is_break == True:
        print('結束了...')
        break
    for i in range(timer):
        print(timer - i)
        time.sleep(1)
    print('0, 結束了...')
    time.sleep(2)
    clearconswin()


#作者:嘉勳
#scratch連結==> (https://scratch.mit.edu/projects/781582138/)
#Windows 適用, 之後會改良
## 請記得使用程式字型... ##