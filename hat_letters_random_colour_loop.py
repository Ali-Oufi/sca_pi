from sense_hat import SenseHat
import time
import random
sense = SenseHat()

line = raw_input("Type a message: ")

for c in line:
    sense.show_letter(c, (random.randint(0,255), random.randint(0,255), random.randint(0,255)))
    time.sleep(1)

sense.clear()
