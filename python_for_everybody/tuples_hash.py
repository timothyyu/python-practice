n=1
integer_list = [n,n+1]
n = len(integer_list)
print(n)
print(integer_list)
t = tuple(integer_list)
print(hash(t))
# integer_list = [int(x) for x in integer_list]
# t=tuple(n,integer_list)
# hash(t)