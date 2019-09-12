#ex21 p.104 functions can return something

def add(a,b):
    print(f"Adding {a} + {b}")
    return a + b

def subtract(a,b):
    print(f"Subtracting {a} - {b}")
    return a - b

def multiply(a,b):
    print(f"Multiplying {a} * {b}")
    return a * b

def divide(a,b):
    print(f"Multiplying {a} / {b}")
    return a / b

print("Let's do some math with just functions!")

age = add(30,5)
height = subtract(78,4)
weight = multiply(90,2)
iq = divide(100,2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

# A puzzle
print("Here is a puzzle:")

what = (add(age,subtract(height,multiply(weight,divide(iq,2)))))
print(f"That becomes {what} Can you do it by hand?")

# figure out the nromal formula that would recreate this same set of operations without nested return function chain calls
what_normal_formula = age + (height-((iq/2) * weight))
print(f"normal formula version result: {what_normal_formula } ")