#print 1,2,3....n without string method and without spaces
n = 3
# print(*[n-2,n-1,n],sep='')
print(*range(1, int(n)+1), sep='')