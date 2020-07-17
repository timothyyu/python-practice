"""
# p.146, excercise 33, "While Loops" (Learn Python The Hard Way)
"""

i = 0
numbers = []

while i < 6:
    print(f"At the top i is {i}")
    numbers.append(i)

    i = i + 1
    print("Numbers now: ", numbers)
    print(f"At the bottom is is {i}")


print("The numbers: ")

for num in numbers:
    print(num)

