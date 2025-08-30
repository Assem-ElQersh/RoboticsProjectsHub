import pynput
import serial
from pynput.keyboard import Key, Controller
keyboard = Controller()
Arduino_Serial = serial.Serial('COM3', 115200)
while 1:
    incoming_data = str(Arduino_Serial.readline())
    print(incoming_data)

    if 'R' in incoming_data:
        keyboard.press(Key.right)
        keyboard.release(Key.right)
    elif 'U' in incoming_data:
        keyboard.press(Key.up)
        keyboard.release(Key.up)
    elif 'L' in incoming_data:
        keyboard.press(Key.left)
        keyboard.release(Key.left)
    elif 'D' in incoming_data:
        keyboard.press(Key.down)
        keyboard.release(Key.down)