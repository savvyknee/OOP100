# Trapezoid.py
#
#	A simple program that takes inputs from a user,
#	does some calculation,
#	and outputs the area of the trapezoid


def main():
	print("Area of a trapezoid")									#print statement
	h = eval(input("Enter the height of the trapezoid: "))			#user input: height of trapezoid
	x1 = eval(input("Enter the length of the bottom base: "))		#user input: length of bottom
	x2 = eval(input("Enter the length of the top base: "))			#user input: length of top
	a = .5 * (x1 + x2) * h											#assignment statement; calculate area from inputs using formula
	print("The area is: ", a)										#print statement, including variable a

main()																#run the method
