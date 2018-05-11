# Python Functions

# Three types of functions
	# Built in functions
	# User-defined functions
	# Anonymous functions 
		# i.e. lambada functions; not declared with def():

# Method vs function
	# Method --> function that is part of a class 
		#can only access said method with an instance or object of said class
	# A straight function does not have the above limitation; insert logical proof here about how all methods are functions
		# but not all functions are methods

# Straight function
	# block of code that is called by name
		# can be passed parameters (data)
		# can return values (return value)
def straightSwitch(item1,item2):
	return item2,item1

class SwitchClass(object):
	# Method
	def methodSwitch(self,item1,item2):
		# First argument of EVERY class method is reference to current instance
		# of the class (i.e. itself, thus 'self')

		self.contents = item2, item1
		return self.contents

# in order to access methodSwitch(), instance or object needs to be defined:

#instance declared of SwitchClass object
instance =  SwitchClass()

#method methodSwitch() called upon instance of the above object
print(instance.methodSwitch(1,2))


# functions ---> data is explicitly passed
# methods ---> data is implicitly passed
# classes ---> are blueprints for creating objects

# function arguments
	# default, required, keyword, and variable number arguments
	# default: take a specified default value if no arguement is passed during the call
	# required: need to be passed during call in specific order
	# keyword: identify arguments by parameter name to call in specified order
	# variable argument: *args (used to accept a variable number of arguements)