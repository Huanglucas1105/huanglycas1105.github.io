import time
import os

input_TM = 0
is_break = 1

def timer():
    global input_TM, is_break
    try:
        input_TM = str(input('設定時間'))
        if input_TM == 0:
            is_break = True

    except ValueError:
