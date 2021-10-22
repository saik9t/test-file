# -*- coding: utf-8 -*-

# Description:
#
# This is the final version guess number game demo program
# The entry point of program starts with main() and being verified
# by __name__.
# The computer generated number is from 1 to x where x is passed
# from guess(x) and x is set to 10 in this listing.
#
# Author: Gui Shengqi
# Date: 21 Oct. 2021

import random   # import the random number package

def main():
    guess(10)  

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input("Enter your guess number, please: "))
        
# Use the list to judge the number, and use the "try" to excute the statement.
        x = [] # make a empty list.
        for i in range(random_number):
            x.append(i) #use the for to make a new list
        try:  # I use "try" to replace "if".
            x[guess] # If guess >= random_number, the code will report error. Otherwise, will not report error.
        except IndexError:
            try: # When guess >= random_number, we should judge the "guess" again.
                x[guess-1]
            except IndexError: # If guess > random_number, the code well report IndexError and excute the following statement
                print("Sorry, guess again. Too high.")
            else: # If guess = random_number, the loop will be broken.
                break
        else: # When guess < random_number
            print("Sorry, guess again. Too low.")
        
            
    print("You have guessed the number", random_number, "correctly!!")
    
if __name__ == '__main__':
    main()
