# Temperature.py
#
#	A temperature converter program that takes input from user
#	converts the input temperature from farenheit to celcius
#	and then prints the output in a message to the user

def main():
	faren = eval(input("Enter temperature in Farenheit: "))  #get the temperature in F to convert to C from user
	celc = (5.0/9.0)*(faren - 32)							 #do the conversion
	print("The temperature in Celsius: ", celc)				 #display the end result

main()														#run the method
