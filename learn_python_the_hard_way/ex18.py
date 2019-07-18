#p.92 ex18 names, variables, code, functions

# this one is like your scripts with argv
def print_two(*args):
    # (*args) tells python take take all the arguments of the function
    # and then put them in args as a list
    arg1,arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")


# In python, you can skip the whole unpacking of arguments,
# and just use the names you want to use inside the ()

#ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# this just takes one arguement
def print_one(arg1):
    print(f"arg1: {arg1}")

# this one takes no arguments
def print_none():
    print("I got nothin'.")

print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()






