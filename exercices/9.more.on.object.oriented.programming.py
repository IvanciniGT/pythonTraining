# We have set already the concept of class and object.

# A class is just a new custom Data Type that we can create.
# An object is an instance of a class.... and actual DATA... of that custom Data Type.

# A Square is a 2D shape that has 4 sides of equal length and 4 right angles.
# A square is characterized by the length of one of its sides.
# And ... we can define functions that apply to a square... 
# like calculating its area or perimeter.
#class Square:

#    def __init__(self, side_length):
#        self.side_length = side_length

#    def area(self):
#        return self.side_length * self.side_length

#    def perimeter(self):
#        return 4 * self.side_length


class Rectangle:

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height

    def perimeter(self):
        return 2 * self.base + 2 * self.height

class Square(Rectangle):

    def __init__(self, side_length):
        ## The super keyword is used to POINT to the parent class.
        super().__init__(side_length, side_length)
        # A Square is just a Rectangle with both base and height equal to the side length.

    def perimeter(self):
        return 4 * self.base # 1 operation instead of 3
    
    # As a rectangle, a square has the same area and perimeter
    # We don't need to redefine the area and perimeter functions
    # because they are already defined in the Rectangle class.
    # And a Square inherits those function from the Rectangle class.

# INHERITANCE (an OOP concept)
# In OOP, we can define a class that inherits from another class. A class that EXTENDS another class.
# The class that inherits is called the child class.
# The class that is inherited from is called the parent class.
# The child class inherits all the attributes and methods of the parent class.
# The child class can also define new attributes and methods.
# The child class can also override methods of the parent class.
##############################################

square1 = Square( 10 )
square2 = Square( 20 )
print(square1.area())
print(square2.area())
print(square1.perimeter())
print(square2.perimeter())


rectangle1 = Rectangle( 10, 20 )
rectangle2 = Rectangle( 20, 30 )
print(rectangle1.area())
print(rectangle2.area())
print(rectangle1.perimeter())
print(rectangle2.perimeter())