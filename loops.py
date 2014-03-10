#										Andrew Savini		CST100		loops.py		8Feb2014
#loops.py
#prints out sequences of digits, according to specifications put forth by assignment 4

def main():

#print digits 0-10, ten times
	def tenRange():
		"Prints numbers 0-9.  Does this ten times, on a separate line each time."
		for i in range(10):
			for i in range (10):
				print (i, end = " ")
			print("\n")

#print each digit(0-9), ten times, on its own separate line
	def tenDigits():
		"Prints each digit from 0-9 ten times, each digit getting its own line."
		for i in range(10):
			j= str(i)
			print((j+" ") *10)

#print lines of digits that grow, incrementing by one, (0-9)
	def ascend():
		"Prints 0, then 0 1, iteratively up through 0-9.  Each iteration getting its own line."
		for i in range(11):
			for j in range (i):
				print (j, end = " ")
			print("\n")

#print the digits that descend, incrementing by one, with a left indents proportional to total
#digits descended (0-9)				
	def descend():
		"Prints 0-9, then 0-8, and so on, iteratively until a line with only 0.  Each iteration gets its own line. \
All lines are indented as many spaces as numbers that have been eliminated.  If we are the fourth line down, \
there are four spaces."
		spaces = " "
		for i in range(10):
			print(end=(spaces*i))
			for j in range(10-i):
				print(j, end=" ")
			print("\n")


#print the digits 10-54, printing the same number of digits on any given line as the number of lines printed
#line one has one number
#line two has two numbers
#each number continues iteration from previous line
#accum stores variable, and is updated with every iteration
	def fiftyFour():
		"Counts from 10 to 54, by one number increments.  Line one gets one number (10), line two gets two numbers \
(11,12) and so on, in that fashion, for ten iterations (ending on 54)"
		accumulator = 9
		for i in range(10):
			for j in range(i):
				accumulator = accumulator+1
				print(accumulator,end=" ")
			print("\n")
	def toContinue():
		"Wait for command to continue."
		input("Press return to continue: ")

	tenRange()
	toContinue()
	tenDigits()
	toContinue()
	ascend()
	toContinue()
	descend()
	toContinue()
	fiftyFour()
	toContinue()

main()
