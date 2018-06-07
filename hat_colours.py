from sense_hat import SenseHat
sense = SenseHat()

yellow = (255,255,0)
blue = (0,0,255)

speed = 0.05

message = "Hello World!"

sense.show_message(message, speed, text_colour=yellow, back_colour=yellow)

sense.clear()
