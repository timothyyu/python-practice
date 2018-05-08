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
instance =  SwitchClass()
print(instance.methodSwitch(1,2))