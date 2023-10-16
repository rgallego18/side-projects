import math #needed math.floor for this
import time

count = 0 
guess = 50
diff = 50 #variable to add or subtract to the guess every time. Shrinks by a factor of 2 every passthrough (50,25,13, 6, 1)
userGuess = " "

print ("Please pick a number in your head between 1 and 100")
time.sleep(1.5)
while (userGuess != "equal"):
    userGuess = str(input("Is your number higher or lower or equal than " + str(guess) + "?: ")).lower() #.lower makes the input all lowercase, easier for keeping track of inputs
    if (userGuess == "higher"):
        if (diff == 1): #if diff is zero it doesn't do anything
            diff = 1
        else:
            diff = math.floor(diff/2)

        guess += diff

        if (guess >= 101): #watching for edge cases
            print("Please try again with a number between 1-100 inclusive")
            break

        count = count + 1
    
    elif (userGuess == "lower"):
        if (diff == 1): 
            diff = 1
        else:
            diff = math.floor(diff/2)
        guess -= diff

        if (guess <= -1): #watching for edge cases
            print("Please try again with a number between 1-100 inclusive")
            break

        count = count + 1

    elif (userGuess == "equal"):
        print("Great! It took " + str(count) + " guesses to guess your number")
        break
    
    elif (userGuess == "quit"):
        break

    else:
        print("Please try again")
        continue

