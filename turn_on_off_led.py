import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
led_pin = 11
GPIO.setup(led_pin,GPIO.OUT)
GPIO.output(led_pin,True)
time.sleep(2)
GPIO.output(led_pin,False)
GPIO.cleanup()
