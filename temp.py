import requests
import base64
import json
import time
import RPi.GPI0 as GPIO


GPIO.setmode(GPIO.BOARD)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while(True):
    if(GPIO.input(13) == 1):
        print(1)


    else:
        print(0)
    time.sleep(0.5)