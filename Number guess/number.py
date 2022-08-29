# Number guessing game
from curses.ascii import isdigit
import random
print("Welcome to Number Guess")
print('*'*40)

upper_bound = input ('Enter upper bound :') # record uppper range of numbers to generate from
if upper_bound.isdigit(): # check if user input is a number
    pass
else:
    print('Enter valid number')

random_number = random.randint(1,int(upper_bound))  # generate random number and store it in a variable
#print(random_number)

guess = None
count= 1 # counter to count number of trials user guesses

while random_number != guess: # while loop to  give user other chances to attempt incase they get it wrong 
    guess = input('Guess a number betwween 1 and '+ str(upper_bound) +':') # variable t store user guess

    if random_number == int(guess):  #check if user guess equals the random number generated
        print("You got it right")
        break
    else:
        print('Try again')
        count +=1
print ('You tried', count,'times')