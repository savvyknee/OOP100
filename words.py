# Andrew Savini		CST100		21Feb2014
# longestWord.py
# creates a list of words typed, finds the longest word, outputs it

def main():

#getTheInput() takes the input from the user.  if the user enters a blank space, it returns a 1, which will reset the program
#otherwise, it returns the input in the form of a list
	def getTheInput():
		"getTheInput() takes input from the user, and enters each word into a list as a separate tuple. In the \
case of a blank line, it resets the program."
		theWords = input("Enter a few words and I will find the longest: \n")
		if theWords == "":
			return 1
		else:
			theWords = theWords.lower()
			words = theWords.split()
			return words

# here, we create a blank new list that will hold the lengths of each tuple in wordList.
# counter is at -1 so we don't have to subtract the one later
# we iterate through each number in legths, looking for a number bigger than the current biggest
# every time biggest is updated, we note the index number of the tuple.  this comes into play later.
	def find_longest_word(wordList):
		"find_longest_word takes one parameter in the form of a list holding strings.  It finds the string with the most characters, and \
returns the index of the word with the most characters.  In the case of there being two words of equal characters, both being tied \
for the biggest, it returns the first."
		lengths = []
		index = 0
		counter = -1
		biggest = 0
		current = 0
		for word in wordList:
			lengths.append(len(word))
		for i in lengths:
			counter += 1
			biggest = i
			if biggest > current:
				current = biggest
				index = counter
		return index

# I wanted to handle the case of a blank line.  The best way I could think of was to create a list called
# words, to hold the returned list from getTheInput() and reset the program in the case of a blank line
# Otherwise, we print a statement, then we print the list.
# Then we print the next statement.
# Lastly, we implement the find_longest_word function with the parameter being the list "words"
# It returns a number value, referencing the index in the list "words" of the tuple with the most characters
	words = getTheInput()
	if words ==1:
		main()
	else:
		print("The list of words entered is:")
		print(words)
		print("The longest word in the list is:")
		print(words[find_longest_word(words)])



main()
