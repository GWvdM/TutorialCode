# Python program to demonstrate
# super function
# https://www.geeksforgeeks.org/python-super/

class Animals:
	# Initializing constructor
    def __init__(self):
        print('parent class --init-- function called')
        self.legs = 4
        self.domestic = True
        self.tail = True
        self.mammals = True
	
    def isMammal(self):
	    if self.mammals:
		    print("It is a mammal.")
    
    def isDomestic(self):
	    if self.domestic:
		    print("It is a domestic animal.")


class Cats(Animals):
    def __init__(self):
        #self.legs = 6 # this will getoverridden by call to parent init function
        self.toes = 12
        super().__init__()
        self.legs = 6 # this will override the parent __init__ values
        '''
        as soon as the class gets its own __init__ function it overrides access to the parent __init__
        we then have to call the parent init function to complete the instantiation of the object

        '''
        self.domestic = False
    def has_spots(self):
        print('does cat have spots')


class Dogs(Animals):
	def __init__(self):
		super().__init__()

	def isMammal(self):
		super().isMammal()

class Horses(Animals):
	def __init__(self):
		super().__init__()

	def hasTailandLegs(self):
		if self.tail and self.legs == 4:
			print("Has legs and tail")

# Driver code
#Tom = Dogs()
#Tom.isMammal()
#Bruno = Horses()
#Bruno.hasTailandLegs()
Pieter = Cats()
Pieter.has_spots()
Pieter.isMammal()
print(Pieter.domestic)
print(Pieter.legs)
print(Pieter.toes)
'''
It is a mammal.
Has legs and tail

'''
'''
parent class --init-- function called
does cat have spots
It is a mammal.
False
6
12

'''