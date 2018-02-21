import os
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)
while True:
        i=GPIO.input(17)
        if i==True:
                print'Systen is going to reboot'
                time.sleep(1)
                os.system('sudo shutdown -r now')
        if i==False:
                print'System ready'
                time.sleep(0.5)
GPIO.cleanup()
