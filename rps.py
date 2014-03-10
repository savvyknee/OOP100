#		 									rps.py		Andrew Savini	CST 100		30Jan2014		Rock Paper Scissors Game.
#
# Player One enters Rock, Paper, or Scissors, then Player Two does as well.
# Determine a winner
# Report and record the winner
# Play again
# Game is Best of Five.  If one player wins 3 rounds, the game is over.
# the game was unfair when player two could see what player one picked
# getpass prevents echo of character chosen
import getpass

def main():
	"The main() method holds the execution flow of the game, global variables, and is where functions are defined."

#Define variables
	gamesCounter = 0


	def game():
		"The game() method is where the users play.  We invoke getpass.getpass to hide the text input by players.\
The game() method collects user input and determines who the winner of the round is.  It then prints \
a message stating who the winner is, and what choice each player made.  Depending on who has won the round, the function \
returns a 1, 2, or 3."
	
#User input must be a legal value, or we start over.
		def verify(string):
			"verify(string) method checks the input for invalid entries.  If entry is good: do nothing. \
If entry is bad, print error, and start again."
			if (string == "PAPER" or string == "ROCK" or string== "SCISSORS"
			or string =="P" or string =="R" or string =="S"): 
				return 1
			else:
				return 0
		try:
#Get input from user.
			playerOne = getpass.getpass("Player 1: Please enter either (R)ock, (P)aper, or (S)cissors: \n")
			playerTwo = getpass.getpass("Player 2: Please enter either (R)ock, (P)aper, or (S)cissors: \n")
#Switch user input to all caps.
			playerOne = playerOne.upper()
			playerTwo = playerTwo.upper()
#Check validity of user input.
			verify(playerOne)
			if verify(playerOne) == 0:
				playerOne = "something they shouldn't have"
			else:
				playerOne = playerOne[0]
			verify(playerTwo)
			if verify(playerTwo) == 0:
				playerTwo = "something they shouldn't have"
			else:
				playerTwo = playerTwo[0]
							
#Rock beats scissors; paper beats rock; rock beats scissors.
			if ((playerOne[0]=="P" and playerTwo[0]=="R")
				or (playerOne[0]=="R" and playerTwo[0]=="S")
				or (playerOne[0]=="S" and playerTwo[0]=="P")):
				print ("Player 1 picked",playerOne,".\nPlayer 2 picked",playerTwo,".\nPlayer 1 wins!\n")
				return 1
			elif ((playerOne[0]=="P" and playerTwo[0]=="S") 
					or (playerOne[0]=="R" and playerTwo[0]=="P") 
					or (playerOne[0]=="S" and playerTwo[0]=="R")):
				print("Player 1 picked",playerOne,".\nPlayer 2 picked",playerTwo,".\nPlayer 2 wins!\n")
				return 2
			elif ((playerOne[0]=="P" and playerTwo[0]=="P")
				or (playerOne[0]=="R" and playerTwo[0]=="R") 
				or (playerOne[0]=="S" and playerTwo[0]=="S")):
				print("Player 1 picked",playerOne,".\nPlayer 2 picked",playerTwo,".\nTie.  Nobody wins.\n")
				return 0
			else:
				print("Player 1 typed",playerOne,".\nPlayer 2 typed",playerTwo,".\nTry again with a valid input.\n")	
		except:
			print("Quit trying to break me!")
			
#this while loop takes the return value from game() and makes it useful
#it tallies the winner, then increments the loop
#in the event of a tie, no tally, but still increment
#in the event of an illegal value, neither increment nor tally
#if there is already a clear winner, exit loop early and go to declaring a winner
	def counter(increments):
		"counter(increments) takes the return value from game() and acts as both a hidden scoreboard, and a counter \
of games played.  When a best of five is determined, the winner is declared, and the scores are shown."
#Set variables for player scores.
		playerOneTotal = 0
		playerTwoTotal = 0
#We're playing best of 5.
		while increments < 5:
#Scoreboard records return value from game().
			scoreboard = game()
#Scoreboard will equal 1 when player one wins a round, so we increment his total. If he's already won 3, we exit the loop.
			if scoreboard == 1:
				playerOneTotal = playerOneTotal +1
				if playerOneTotal == 3:
					increments = 5
				else:
					increments = increments +1
#Same as 1, but 2.
			elif scoreboard ==2:
				playerTwoTotal = playerTwoTotal +1
				if playerTwoTotal == 3:
					increments = 5
				else:
					increments = increments +1
#Scoreboard equals 0 when there's a tie.  No score is added, but counter increments.
			elif scoreboard ==0:
				increments = increments+1
#If something is broken, we won't count that against games played.
			else:
				increments = increments
#When increments equals 5, the game is over.  Either there is a winner, or there are two losers.
		if increments == 5:
			if playerOneTotal > playerTwoTotal:
				print("Player One Wins! ", playerOneTotal, "matches to ",playerTwoTotal,".")
			elif playerTwoTotal > playerOneTotal:
				print("Player Two Wins!  ", playerTwoTotal, "matches to ",playerOneTotal,".")
			else:
				print("Tie Score! You're both losers!")



#this is the actual beginning of the execution		
	print("Rock, Paper, Scissors.\nBest of Five Rounds.\n****How To Play:****\nYou will not see what "
			"character you type until the round is over.\nPlease enter your selection.\n"
			"Then press <Enter>\nGo!")
	game()
	counter(gamesCounter)
main()
