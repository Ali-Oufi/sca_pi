from sense_hat import SenseHat
sense = SenseHat()
import time
import random

times = int(raw_input("How many random pixels do you want to be selected? "))

while times>0:
    x = random.randint(0,7)
    y = random.randint(0,7)
    sense.set_pixel(x,y,(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
    time.sleep(1)
    sense.set_pixel(x,y,(0,0,0))
    times = times - 1

