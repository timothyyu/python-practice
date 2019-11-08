# https://www.patricksoftwareblog.com/python-unit-testing-structuring-your-project/
class BasicFunction(object): 
    def __init__(self): 
        # initial state of object created with class has state of 0
        self.state = 0
 
    def increment_state(self): 
        # method to increment class object state by +1
        self.state += 1
 
    def clear_state(self): 
        # method to clear state of class object/reset to 0/default
        self.state = 0
    
    def decrement_state(self): 
        # method to decrement class object state by -1
        self.state -= 1