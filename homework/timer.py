import time
import os

clock = 0
is_break = 1

def timer():
    global clock, is_break
    try:
        clock = str(input('設定時間'))
        if clock == 0:
            is_break = True

    except ValueError:
        print('再試一次')
        timer()

def clearscreen():
    os.command('cls')

def timercount():
    global clock
    for i in range(clock):
        time.sleep(1)
        print(clock - i)
    clearscreen()
while True:
    clearscreen()
    timer()
    if is_break == True:
        break
    timercount()