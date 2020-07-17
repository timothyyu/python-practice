"""
# p.132, excercise 28, "Boolean Practice" (Learn Python The Hard Way)
"""
p=[]
#1
p.append( True and True) # True
#2
p.append( False and True) # False
#3
p.append( 1 == 1 and 2 == 1) # False
#4
p.append( "test" == "test") # True
#5
p.append( 1 == 1 or 2 != 1) # True
#6
p.append( True and 1 == 1) # True
#7
p.append( False and 0 != 0) # False
#8
p.append( True or 1 == 1) # True
#9
p.append( "test" == "testing") # False
#10 
p.append( 1 != 0 and 2 == 1) # False
#11
p.append( "test" != "testing") # True 
#12
p.append( "test" == 1) # False 
#13
p.append( not (True and False)) # True
#14
p.append( not ( 1 == 1 and 0 != 1)) # False 
#15
p.append( not ( 10 == 1 or 1000 == 1000)) # False
#16
p.append( not ( 1 != 10 or 3 == 4)) # False
#17
p.append( not ("testing" == "testing" and "Zed" == "Cool Guy")) # True
#18
p.append( 1 == 1 and (not ("testing" == 1 or 1 == 0))) # True
#19
p.append( "chunky" == "bacon" and (not (3 == 4 or 3 == 3))) # False
#20
p.append( 3 == 3 and (not ("testing" == "testing" or "Python" == "Fun"))) # False

for i in range(0,len(p)):
    print(i+1,p[i])

"""
p.133 More Complex Boolean Logic Statement Solving process:

1. Find an equality test (== or !=) and replace it with its truth.
2. Find each and/or inside parentheses and solve those first.
3. Find each not and invert it.
4. Find any remaining and/or and solve it.
5. When you are done you should ahve True or False.
"""