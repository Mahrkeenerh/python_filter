from pynput.keyboard import Listener
from threading import Thread
import json
from . import ImageFilter

running = False
pressed = {}
pressed_pause = {}
shortcut = []
pause_shortcut = []


def load():

    global shortcut, pressed, pause_shortcut, pressed_pause

    with open("source/config.json") as json_file:
        config = json.load(json_file)

    shortcut = config["shortcut"]
    pause_shortcut = config["pause"]

    for s in shortcut:
        pressed[s] = False
    
    for s in pause_shortcut:
        pressed_pause[s] = False


def on_press(key):

    global running, pause_shortcut, shortcut, pressed_pause, pressed

    strip_key = str(key).replace("'", "")

    if strip_key in shortcut:
        for s in shortcut:
            if s == strip_key:
                pressed[s] = True
                break

            if not pressed[s]:
                break
    
    if strip_key in pause_shortcut:
        for s in pause_shortcut:
            if s == strip_key:
                pressed_pause[s] = True
                break
            
            if not pressed_pause[s]:
                break

    if all(list(pressed.values())):
        if not running:
            Thread(target=ImageFilter.run).start()
        else:
            ImageFilter.close()
        
        for s in shortcut:
            pressed[s] = False
    
        running = not running

    if all(list(pressed_pause.values())):
        ImageFilter.pause()
    
        for s in pause_shortcut:
            pressed_pause[s] = False


def on_release(key):

    global shortcut, pause_shortcut, pressed, pressed_pause

    strip_key = str(key).replace("'", "")

    if strip_key in shortcut:
        pressed[strip_key] = False
    
    if strip_key in pause_shortcut:
        pressed_pause[strip_key] = False


def run():

    load()

    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
