#	Andrew Savini		CST100		23Feb2014		numbers.py
#	Takes a bunch of numbers that the user enters, computes their total average, the average of the positive numbers, and the averages
#	of the negative numbers, then outputs the list of numbers and the key:value dictionary entries of everything.

def main():

# get a list of numbers from the user
# -9999 is the sentinel value.  when entered, we exit the while loop
# otherwise each number is appended to listOfNumbers list
# program returns a list of user inputted numbers
	def getNumbers():
		"getNumbers() prompts the user for numbers, entering the numbers in a returned list.  Sentinel value \
is -9999."
		numList = []
		numbers = 0
		while numbers != -9999:
			try:
				numbers = eval(input("Enter a number(-9999 to end):"))
			except:
				print("You have entered an illegal value.  Terminating.")
				return 1
			if numbers < -9999 or numbers > -9999:
				numList.append(numbers)
			elif numbers == -9999:	
				return numList


# Use numbers in numList to find the average of all numbers
	def allNumAvg(numList):
		"allNumAvg(numList) takes the numbers input originally and computes their average."
		counter = 0.0
		runningTotal = 0.0
		finalAvg = 0.0
		for i in numList:
			counter += 1
			runningTotal = runningTotal + i
		finalAvg = runningTotal/counter
		return finalAvg

# Use numbers in numList to find the average of all the positive numbers in numList
# If there are no positive numbers, we change the counter to a 1, so we are not dividing by 0, avoiding an error.
	def posNumAvg(numList):
		"posNumAvg(numList) takes only the positive numbers input by user to compute the average."
		counter = 0.0
		runningTotal = 0.0
		finalAvg = 0.0
		for i in numList:
			if i >= 0.0:
				counter += 1
				runningTotal = runningTotal + i
		if counter == 0:
			counter = 1
		finalAvg = runningTotal/counter
		return finalAvg

# Use numbers in numList to find the average of all the negative numbers in numList
# If there are no negative numbers, we change the counter to a 1, so we are not dividing by 0, avoiding an error.
	def nonPosAvg(numList):
		counter = 0.0
		runningTotal = 0.0
		finalAvg = 0.0
		for i in numList:
			if i < 0.0:
				counter += 1
				runningTotal = runningTotal + i
		if counter == 0:
			counter =1
		finalAvg = runningTotal/counter
		return finalAvg


	inputNumbers = getNumbers()
# If the user enters anything other than a number, we exit the program.  Ain't nobody got time for that.
	if inputNumbers == 1:
		return

# Create the dictionary with key:value pairs
	dictionary = {'AvgPositive':0,'AvgNonPos':0,'AvgAllNum':0}
# Change the dictionary values to reflect the computed averages as input by the user
	dictionary['AvgAllNum'] = allNumAvg(inputNumbers)
	dictionary['AvgPositive'] = posNumAvg(inputNumbers)
	dictionary['AvgNonPos'] = nonPosAvg(inputNumbers)
# Provide the user with some output
	print("The list of all the numbers entered is: ")
	print(inputNumbers)
	print("The dictionary with averages is:")
	print(dictionary)

main()
