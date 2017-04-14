# Excercise 4, Ch. 4 Pg. 55, Python For Informatics v3

# Rewrite the grade program from the previous chapter using a function
# called computegrade that takes a score as its parameter and returns
# a grade as a string

score = input("Enter a numeric grade from 0 to 100: ")

def computegrade(score):
    score = float(score) / 100
    if score > 1.0 :
        return ('Score out of range')
        exit()
    elif score >= 0.9 :
        return ('A')
    elif score >= 0.8 :
        return ('B')
    elif score >= 0.7 :
        return ('C')
    elif score >= 0.6 :
        return ('D')
    elif score < 0.6 :
        return ('F')

print (computegrade(score))
# Same as above print statement, but using the format operator:
# print ('%s' % computegrade(score))

