

from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(6, GPIO.IN)

leds = GPIO.input(6)

while True:
   f= open("f.txt", "w")
   f.write("dict = " + repr(dict) + "/n")
   f.close
   
   tempRead( leds)
   
   print(tempRead)
   
   sleep(2)