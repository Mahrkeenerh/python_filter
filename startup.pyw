# Python Nvidia GPU accelerated program to apply a filter on display (show HSV value)
# Samuel Buban
# Pixel Federation
# 31.8.2021


from infi import systray
from source import KeyLogger
from threading import Thread
from infi.systray import SysTrayIcon
import os


def exit(systray):
    os._exit(0)


Thread(target=KeyLogger.run).start()

systray = SysTrayIcon("source/v.ico", "Image Filter", (), on_quit=exit)
systray.start()
