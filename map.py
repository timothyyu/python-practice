# Map function

# http://book.pythontips.com/en/latest/map_filter.html

l = [1,2,3]

#float(l) 

# Results in error: 
	# TypeError: float() argument must be a string or a number, not 'list'

# Cannnot use float() directly on a list (arg must be a string or num)
	# use map instead 

lf = list(map(float,l))
print (lf)
