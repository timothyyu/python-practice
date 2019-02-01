#p68-69 ex 11

print("How old are you?", end=' ')
age=input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()


# end = ' ' @ the end of end print line tells
# print to NOT end the line with a newline 
# character and go to the next line.
print(f"So, you're {age} old, {height} tall and {weight} heavy.")