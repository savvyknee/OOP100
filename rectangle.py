#	Andrew Savini	CST 100		25Feb2014		rectangle.py
#	Create a class named 'Rectangle' with the assigned attributes and methods

class Rectangle:
	"""Rectangle is a class that creates a rectangle"""


# Set the initial values for when the object is created
	def __init__(self, x, y, width, height):
		"__init__(self,x,y,width,height) takes four parameters and sets their values to those of the Rectangle object you \
are creating."
		self.x = x
		self.y = y
		self.w = width
		self.h = height


# Return a string describing the object
	def __str__(self):
		"__str__(self) needs no parameters.  It governs the description given when object is printed."
		return "Rectangle("+str(self.x)+","+str(self.y)+","+str(self.w)+","+str(self.h)+")"


# Return the value of the right edge of the rectangle
	def right(self):
		"right(self) takes no parameters.  It returns the value of the right edge of the object."
		return (self.w + self.x)

# Return the value of the bottom edge of the rectangle
	def bottom(self):
		"bottom(self) takes no parameters.  It returns the value of the bottom edge of the object."
		return (self.h + self.y)

# Return the width and height of the rectangle 
	def size(self):
		"size(self) takes no parameters.  It returns the height and width of the object."
		return (self.w,self.h)

# Return the x and y coordinates of the rectangle
	def position(self):
		"position(self) takes no parameters.  It returns the x and y coordinates of the rectangle."
		return(self.x,self.y)

# Return the x and y coordinates of the rectangle
	def area(self):
		"area(self) takes no parameters.  It multiplies height and width to give area of the rectangle."
		return(self.h*self.w)

# Take an offset value and return a copy of the rectangle expanded with offset in all directions
	def expand(self, expand):
		"expand(self, expand) takes one integer or float parameter, and applies it to expand and offset the rectangle in all directions."
		expandedH = self.h + (expand*2)
		expandedW = self.w + (expand*2)
		offsetX = self.x - expand
		offsetY = self.y - expand
		return(Rectangle(offsetX,offsetY,expandedW,expandedH))

# A program to illustrate the operations performed by the methods of class Rectangle.
def main():

# Call a Rectangle with values given, then print.
	r = Rectangle(5,10,50,100)
	print ("r = "+str(r))

# A pause I will use to break up the assignment
	stop = input("Press enter: ")

	r2 = Rectangle(5,10,50,100)
	print ("r2 = "+str(r2))

	stop = input("Press enter: ")

# A demonstration of the Rectangle.right(self) method
	r3 = Rectangle(3,5,10,20)
	print ("r3 = "+str(r3))
	print ("r3.right() = "+str(r3.right()))

	stop = input("Press enter: ")

# Another demonstration of the Rectangle.right(self) method
	r4 = Rectangle(12, 10, 72, 35)
	print("r4 = "+str(r4))
	print ("r4.right() = "+str(r4.right()))

	stop = input("Press enter: ")

# A demonstration of the Rectangle.bottom(self) method
	r5 = Rectangle(5, 7, 10, 6)
	print("r5 = "+str(r5))
	print ("r5.bottom() = "+str(r5.bottom()))

	stop = input("Press enter: ")

# A demonstration of the Rectangle.bottom(self) method's mutability
	r5.y += 12
	print("r5.y += 12")
	print("Now, r5 = "+str(r5))
	print ("So, r5.bottom() = "+str(r5.bottom()))

	stop = input("Press enter: ")

# Demonstrations of Rectangle.size(self), Rectangle.postion(self), and Rectangle.are(self)
	r6 = Rectangle(1,2,3,4)
	print("r6 = "+str(r6))
	print ("r6.size() = "+str(r6.size()))
	print ("r6.position() = "+str(r6.position()))
	print ("r6.area() = "+str(r6.area()))

	stop = input("Press enter: ")

# Demonstration of the Rectangle.expand(self, offset) method 
	r = Rectangle(30, 40, 100, 110)
	print("r = "+str(r))

# Note the new Rectangle object created, and the unaltered original Rectangle object, r.
	r1 = r.expand(3)
	print ("r1 = r.expand(offset =3)\nr1 ="+str(r1))
	print("r = "+str(r))

	stop = input("Press enter: ")

# Showing Rectangle.expand(self, offset) using a negative value.
	r2 = r.expand(-5)	
	print ("r2 = r.expand(offset= -5) \nr2 ="+str(r2))
		
main()
