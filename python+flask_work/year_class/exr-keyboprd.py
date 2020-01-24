from pynput.keyboard import Key, Listener

from kke import listener


def on_press(key):
    if key is Key.backspace = ' ':
        print(key)


with Listener(on_press=on_press):
    listener.join()