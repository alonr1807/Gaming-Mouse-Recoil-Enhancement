import pynput
from pynput.keyboard import Key, Listener
from pynput import mouse
import serial
from pynput import keyboard
from threading import Thread
import signal

arduino = serial.Serial('COM3', 9600, timeout=.1)
listener = None
interrupted = False
def signal_handler(signal, frame):
    print("interrupted")
    global interrupted
    interrupted = True


def on_click(x, y, button, pressed):
    if interrupted:
        return False
    if not button == mouse.Button.left:
        return True
    if pressed:
        arduino.write(bytes("1", 'utf-8'))
        
    if not pressed:
        arduino.write(bytes("2", 'utf-8'))
        return True
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))
signal.signal(signal.SIGINT, signal_handler)



# ...or, in a non-blocking fashion:
# listener = mouse.Listener(on_click=on_click)
# listener.start()1

with mouse.Listener(on_click=on_click) as listener:
    listener.join()




















































