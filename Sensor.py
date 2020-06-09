

from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

sensor = 3

GPIO.setup(sensor, GPIO.OUT)

try:

print("module ready")

sleep(3)


   f= open("f.txt", "r")
   lines = f.readlines()
   f.close
   
   def read_temp():
   temp_string = sensor
   temp_c = float(temp_string)/1000.0
   
  while True:
  print(read_temp())
  sleep(3)
  
  if GPIO.output(sensor, GPIO.OUT):
  print("sensed")
  
  sleep(3)
  
  except KeyboardInterrupt:
  print("stopped")
  GPIO.cleanup()
  
   