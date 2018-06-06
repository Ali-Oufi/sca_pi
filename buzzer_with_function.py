import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
buzz_pin = 32
GPIO.setup(buzz_pin,GPIO.OUT)
Buzz = GPIO.PWM(buzz_pin,1000)
def buzz(freq):
    Buzz.ChangeFrequency(freq)
    Buzz.start(50)
    time.sleep(1)
    Buzz.stop()
buzz(440)
buzz(880)
GPIO.cleanup()
