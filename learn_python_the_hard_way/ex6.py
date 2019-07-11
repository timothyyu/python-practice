# p.52 ex6 strings and text

# Set types_of_people to 10
types_of_people = 10
# f-string with types_of_people
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
# f-string with two string variables in-line
y = f"Those who know {binary} and those who {do_not}."

# print both f-strings
print(x)
print(y)

print(f"I said: {x}")
print(f"I also said '{y}'")


# print variable  with formatted string
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

# concat of of two strings print output
print (w + e)