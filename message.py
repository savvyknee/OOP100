#Andrew Savini		00CST100		8Feb2014		
#messages.py
#takes input from user to encode messages using ascii dictionary
#takes encoded messages from user and decodes them using ascii dictionary

def main():

#stores user input message in toEncode, stores value for user input offset in offset
#takes each character in toEncode, gets the ascii integer, adds the offset, prints it
#throws exception for blank line
#throws error and try again for out of range in offset
	def encode():
		"User enters a message to encode, then an offset.  Encode() converts character to ASCII ordinal, \
adds the offset, converts back to a character, and prints the message.  Errors are thrown for out of range \
and for blank lines."
		try:
			toEncode = input("Enter message to encode:\n")
			offset = eval(input("Enter a key value(between 0 and 100) for encoding:\n"))
			if offset < 0 or offset > 100:
				print("Offset out of range.  Start again.")
				encode()
			else:
				for char in toEncode:	
					tempChar = ord(char)+offset
					print(chr(tempChar), end ="")
				print("\n")
		except:
			print("Please enter legal values.\n")
			encode()


#this takes the encrypted message from the user, first.
#then it populates a list with all of the integers from 0 to 127 in the key[]
#for each item in key, it prints the index of the item
#	i did this in the event that i created a message in encode, and knew the offset,
#	i could check the proper offset for both encode and the right number of guesses in decode
#then, we apply the algorithm for the enoded message to each character, for every possibility in the ASCII dictionary.
#Lastly, we print every possibility.
#We throw an error message for blank input.
	def decode():
		"decode() takes the encrypted message from the user, creates a key of 128 ordinal numbers, checks the \
characters of the encoded message against all possibilities in the known algorithm, and displays converted messages \
for interpretation by the user." 
		toDecode = input("Enter an encrypted message to decode:\n")
		if toDecode == "":
			print("You didn't enter a message.  Try again.")
			decode()
		else:
			key = []
			for i in range(128):
				key.append(i)
			for j in key:
				print (j,": ")
				for char in toDecode:
					if ((ord(char)-j)<32):
						decodedChar = (((ord(char)-j)+127)-32)
					else:
						decodedChar = (ord(char)-j)
					print(chr(decodedChar), end="")
				print("\n")


#This function was added to allow users to select from encode, decode, or quit. 
	def select():
		"select() method takes one letter inputs to direct the flow of the program."
		try:
			pickOne = input("Press 'e' if you'd like to encode a message.\n\
Press 'd' if you need to decode a message.\n\
Press 'q' if you'd like to quit: ")
			pickOne = pickOne.lower()
			if pickOne == "e":
				encode()
				select()
			elif pickOne == "d":
				decode()
				select()
			elif pickOne =="q":
				return
			else:
				print("Illegal.  Try Again.")
				main()
		except:
			print("Something crazy happened.  Start over.")
			main()
	select()

main()
