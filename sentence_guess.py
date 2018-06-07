from sense_hat import SenseHat
sense = SenseHat()

speed = 0.01
tries = True
message = "Hello World!"

while tries:
    sense.show_message(message,speed,(255,255,0),(0,0,0))
    guess = raw_input("Guess the phrase: ")
    if guess == message:
        tries = False
    speed = speed + 0.005
print "Congrats, you guessed it!"
