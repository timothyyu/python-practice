# print 2nd highest score/value
    # 6 is highest
    # 5 is desired output
n = 5
arr = [2,3,6,6,5]

print (sorted(list(set(arr)))[-2])
    # set removes duplicates
    # list from map method
    # sorted() ---> [-2] for 2nd highest for ascending order