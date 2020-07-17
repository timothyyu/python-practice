
"""
# p.126, excercise 26 (Learn Python The Hard Way)
      # python ex26.py ex26.py

'Your job in this exercise is to correct this fle. 
Use all of your skills to make this fle better. 
Analyze it first, maybe printing it out to edit it like you would a school term paper. 
Fix each ﬂaw and keep running it and fxing it until the script runs perfectly.'
"""
  
from sys import argv

print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")

script, filename = argv
txt = open(filename)

print("Here's your file {filename}:")
print(txt.read())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)
def print_all(f):
    print(f.read())
print_all(txt_again)


print('Let\'s practice everything.')
print('You\'d need to know \'bout escapes\n\
    with \\ that do: \n\n newlines and \t tabs.')

poem = """
  The lovely world 
with logic so firmly planted 
cannot discern \n the needs of love 
nor comprehend passion from intuition 
and requires an explanation
\n\t\t where there is none.
"""

print("--------------")
print(poem)
print("--------------")

five = 10 - (2 + 3)
print(f"This should be five: {five}")

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 10000

beans, jars, crates = secret_formula(start_point)
start_point = start_point / 10
# remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
# it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

print("We can also do that this way:")
formula = secret_formula(start_point)
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))



people = 20
cats = 30
dogs = 15

if people < cats:
    print ("Too many cats! The world is doomed!")

elif people > cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

elif people > dogs:
    print("The world is dry!")


dogs += 5

if people == dogs:
    print("People are equal to dogs.")

elif people >= dogs:
    print("People are greater than or equal to dogs.")

elif people <= dogs:
    print("People are less than or equal to dogs.")


