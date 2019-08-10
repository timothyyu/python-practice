#  You are given three integers x,y,z representing the dimensions of a cuboid along with an integer n . 
#  You have to print a list of all possible coordinates 
#  given by (i,j,k) on a 3D grid where the sum of (i,j,k)  is not equal to n. 
 
x = 1
y = 1
z = 1
n = 2
print(x,y,z,n,sep='\n')

print ([[a,b,c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if a + b + c != n ])