

from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(4, GPIO.OUT)

GPIO.output(4,GPIO.HIGH)


while True:


   f = open("f.txt", "r")
   lines = f.readlines()
   f.close v       
   
   temp_string  = GPIO.input(4)
   temp_string  = float(temp_string) + 0.00
   
   if GPIO.input (4):
       print("sensed")
	   
	   print(temp_c)
	   
	   time.sleep(1)
  
   