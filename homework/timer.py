import time
import os

input_TM = 0


def timer():
    global input_TM
    try:
        input_TM = str(input('設定時間'))
    except ValueError