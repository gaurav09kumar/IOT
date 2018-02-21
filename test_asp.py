import serial
import RPi.GPIO as GPIO
import os, time
led1=17

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(led1, GPIO.OUT)



Serial = serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout=2)
data1=""
data=''
while 1:
        data = Serial.read(1)
        data1+=data
        print data
	if data == '1':
		GPIO.output(led1,True)
		print('Led on')

	if data == '2':
		GPIO.output(led1,False)
		print('Led off')

        Serial.flush();
        data="";
        data1="";

