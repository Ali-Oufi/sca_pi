from sense_hat import SenseHat
import time
import random
sense = SenseHat()

sense.show_letter("H", (random.randint(0,255), random.randint(0,255), random.randint(0,255)))
time.sleep(1)
sense.show_letter("i", (random.randint(0,255), random.randint(0,255), random.randint(0,255)))
time.sleep(1)
sense.show_letter("!", (random.randint(0,255), random.randint(0,255), random.randint(0,255)))
time.sleep(1)

sense.clear()
