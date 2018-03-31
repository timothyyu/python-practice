#Understanding dictionaries and tuples
	#i.e.the relationship/key differences between dict, list, tuple)

#Tuples are immutable, comparable, and hashable
	#can't modify the elements of a tuple, but you can replace a tuple with another tuple

#creation of dictionary
d = {'a':10,'b':1,'c':22}
#dict method that teruns a list of tuples 
	#where each tuple is a key-value pair
t = list(d.items())

print("dict:", d)
print("tuple return:",t)

#accessing single element(s) from dict, but through list method
	#that returns result as tuple:
print(t[0])
print("accessing indiviual elements of of the dict through list method (through a tuple):")
print(t[0][0])
print(t[0][1])

#d.items() --> list of tuples  ---> tuples are comparable --> sort methods now applicable

#d.sort() will not work, but:
t.sort()
print(t) #will work (tuples are comparable)

t.sort(reverse=True)
print(t) #will work (tuples are comparable)