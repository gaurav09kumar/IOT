import serial
Serial = serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout=2)
data1=""
data=''
while 1:
    data = Serial.read(1)
    data1+=data
  	print data1


  	Serial.flush();
  	data="";
  	data1="";
