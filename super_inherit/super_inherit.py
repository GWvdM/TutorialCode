
'''
Source: https://realpython.com/python-super/
While the examples above (and below) call super() without any parameters, 
super() can also take two parameters: 
  - the first is the subclass, 
  - and the second parameter is an object that is an instance of that subclass.
'''

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

# here we declare that the Square class inherits from the rectangle class
class Square(Rectangle):

    def __init__(self, length):             # this states that the square class will be instanciated with one parameter --> length
        # super().__init__(length, length)    # we then instantiate the super class with two parameters --> length, length
        super(Square,self).__init__(length, length)      # the super class does not need to be named, as the class is created from it?

'''
In Python 3, the super(Square, self) call is equivalent to the parameterless super() call. 
The first parameter refers to the subclass Square, while the second parameter 
refers to a Square object which, in this case, is self. 
You can call super() with other classes as well:

'''

class Cube(Square):
    def surface_area(self):
        #face_area = super().area()
        face_area = super(Square,self).area()
        '''
        In this example, you are setting Square as the subclass argument to super(), 
        instead of Cube. This causes super() to start searching for a matching method 
        (in this case, .area()) at one level above Square in the 
        instance hierarchy, in this case Rectangle.
        In this specific example, the behavior doesn't change. But imagine that Square 
        also implemented an .area() function that you wanted to make sure Cube did not use. 
        Calling super() in this way allows you to do that
        '''
        return face_area * 6

    def volume(self):
        face_area = super().area()
        return face_area * self.length

'''
previous independant class for square
superceded by super class inheritance

class Square:
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length

    def perimeter(self):
        return 4 * self.length
'''
square = Square(4)
print(square.area()) 
'''
16
'''

rectangle = Rectangle(2,4)
print(rectangle.area())
''''
8
'''

cube = Cube(3)
print(cube.surface_area())
'''
54
'''
print(cube.volume())
'''
27
'''
