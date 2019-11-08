# four sample programming/coding tests:

# 1) create a unique sum from a given array. if a number repeats, find the lowest unique number for the array, and then return the sum.

# 2) find the sum of two fractions and return the lowest divisible fraction

# 3) represent the three following values/strings in binary representations

# 4) return true if a number is prime, and if not/false, return the lowest number that goes into into it


#########################################################
import numpy as np

# 1) create a unique sum from a given array. if a number repeats, find the lowest unique number for the array, and then return the sum.
# given_array = [1,2,2,4,4,9,7,7]
given_array = [1,2,2,4,4,9,7]

def usum_ga(given_array):

    u, c = np.unique(given_array,  return_counts=True)
    u2, c2 = np.unique(given_array,  return_inverse=True)
    # print(u2,c2)
    # print(u2[c2])
    dup = u[c > 1]
    if dup.size > 0:
        min_dup= min(dup)
        # print(dup)
        min_dup_remove = np.delete(given_array,min_dup)
        # print(min_dup_remove)
        # print(sum(min_dup_remove))
        # print(min_dup)
        return (min_dup,sum(min_dup_remove),min_dup_remove)
    
    else:
        return min(u),sum(u)
print(usum_ga(given_array))