import os

ix = raw_input("Type a word: ")
os.system('clear')
length = len(ix)
x = ix.lower()
y = ""
triesw = "0"
guess = ""
z = x
location = -1

while int(triesw) < 1:
    triesw = raw_input("How many tries do you want? ")
tries = int(triesw)

while length > 0:
    y = y + "-"
    length = length - 1

if (" " not in x) & ("-" not in x) & ("1" not in x) & ("2" not in x) & ("3" not in x) & ("4" not in x) & ("5" not in x) & ("6" not in x) & ("7" not in x) & ("9" not in x) & ("0" not in x):
    while ( not (tries==0)) & ( not (x==y)):
        guess = raw_input("Guess a letter: ").lower()
        while not (len(guess) == 1):
            guess = raw_input("Guess a letter: ").lower()
        while guess in z:          
            location = z.find(guess)
            y = y[:location] + guess + y[location + 1:]
            z = z[:location] + "-" + z[location + 1:]
        tries = tries - 1
        print "Your current phrase is", y, ", and you have", tries, "tries."
    if x==y:
        print "You Win!"    
    else:
        print "You Lose!"
        print "The correct word was:", x
else:
    print "Not a word."
