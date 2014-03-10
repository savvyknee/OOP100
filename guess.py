# 														guess.py	CST 100	Andrew Savini	01Feb2014
# 
# The program will generate a pseudo-random number.  
# User gets three tries to guess the number.
# Program tells user whether guess was high, low, or dead on.
# Program prompts to exit, or play more.

import random

def main():
	"Main method holds all of the execution, and contains the two methods (game, and playMore) that govern the flow of the game."

# while number of attempts are 1, 2, or 3, we play the game
# the user inputs their guess.  if too high, or too low, we print a message, and increment numberAttempts
# is the guess is correct, we increment higher than the while loop (5) to exit
# if the user inputs something illegal, we start the function over with no penalty
# if the user fails for 3 guesses, print a message saying the game is over, and what the number was
# if the user inputs something all kinds of wrong, throw an exeption
	def game():
		"The game function is the primary function of the guessing game.  It produces a random number, tells you whether your number is too high\
 or too low.  It is where we print the win or lose messages, determines if a legal value was entered, and keeps track of how many attempts you've\
 had." 
		number = random.randrange(1,20)
		numberAttempts = 1
		while numberAttempts < 4:
			try:
				guess = eval(input("Take a guess.\n"))										
				if guess < number and guess < 21 and guess >= 1:
					print("Your guess is too low.\n")
					numberAttempts= numberAttempts+1
				elif guess > number and guess < 21 and guess >= 1:
					print("Your guess is too high.\n")
					numberAttempts= numberAttempts+1
				elif guess == number:
					if numberAttempts > 1:				
						print("Good job,", name,"!  \nYou guessed my number in", numberAttempts,"guesses!\n")
						numberAttempts = 5
						return
					else:
						print("Good job,", name,"!  \nYou guessed my number in", numberAttempts,"guess!\n")
						numberAttempts = 5				
						return
				else:
					print("Your guess was out of the range of possible answers.\n This try won't count against you.\nTry again.")
			except:
				print("Your guess was not a legal value.\nThis try won't count against you.\nTry again.")
		if numberAttempts == 4:
			print("Your three guesses are over. The number I was thinking of was ", number,".\n")
			return

# a chance to play again
# if yes, call the main function
# if no, quit
# if anything else, print an error message
	def playMore():
		"The playMore function is where the user inputs a y to play again (invoking the main method and resetting the numberAttempts variable)\
, or n to quit.  It also determines if an illegal value was entered (in that case, it will call itself to begin again)." 
		again = input("Would you like to play again?\n")
		if again[0] == "y" or again[0] == "Y":
			numberAttempts = 1
			main()
		elif again[0] == "n" or again[0] == "N":
			return()
		else:
			print("You have entered an illegal value.  Please enter y or n.")
			playMore()



# These are the instructions for the general flow of the game.
# Deliver input message to get player's name.
# The the player how to play in the print message.
# Execute the game() method
# After game() method runs through, execute the playMore() method
	name = input("Hello!  What is your name?:\n")
	print("Well, ", name, " I am thinking of a number between 1 and 20.\n")
	game()
	playMore()

main()
