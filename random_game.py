import random
import RPi.GPIO as GPIO
import time

rand_num = random.randint(1,10)
tries = True
while tries:
    guess = int(raw_input("Guess a number from 1 to 10: "))
    if rand_num<guess:
        print "Guess is too high"
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        buzz_pin = 32
        GPIO.setup(buzz_pin,GPIO.OUT)
        Buzz = GPIO.PWM(buzz_pin,1000)
        Buzz.ChangeFrequency(440)
        Buzz.start(50)
        time.sleep(1)
        Buzz.stop()
        GPIO.cleanup()
    else: 
        if guess<rand_num:
            print "Guess is too low"
            GPIO.setmode(GPIO.BOARD)
            GPIO.setwarnings(False)
            buzz_pin = 32
            GPIO.setup(buzz_pin,GPIO.OUT)
            Buzz = GPIO.PWM(buzz_pin,1000)
            Buzz.ChangeFrequency(440)
            Buzz.start(50)
            time.sleep(1)
            Buzz.stop()
            GPIO.cleanup()
        else:
            print "You guessed it"
            tries = False
            GPIO.setmode(GPIO.BOARD)
            GPIO.setwarnings(False)
            led_pin = 11
            GPIO.setup(led_pin,GPIO.OUT)
            GPIO.output(led_pin,True)
            time.sleep(2)
            GPIO.output(led_pin,False)
            GPIO.cleanup()
