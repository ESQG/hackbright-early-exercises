# Put your code here
import random

name = raw_input("Howdy, what's your name? ")

best = 0

while True:
    print "%s, I'm thinking of a number between 1 and 100." % name
    print "Try to guess my number."
    number = random.randint(1, 100)
    tries = 0

    while True:
        try:
            guess = int(raw_input("Your guess? "))
        except ValueError:
            print "Please enter an integer! "
            continue

        if guess > 100 or guess < 1:
            print ("Can't you remember a simple instruction? I said the number must be from 1 to 100!")
            continue

        tries += 1
        if guess == number:
            print "Well done, %s! You found my number in %i tries!" % (name, tries)
            break
        elif guess > number:
            print "Your guess is too high, try again."
        else:
            print "Your guess is too low, try again."
    if best > tries or best == 0:
        best = tries
    if raw_input("Would you like to keep playing? Yes or no: ").strip().lower() != 'yes':
        break

print "Your best score was %i tries!" % best