# Python 2.7
# Greatest_common_factor
# Test cases
    # (100, 200)
    # (2, 6)
    # (100, 50)
    # (20, 30)

# Solution 1
def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x

print gcd(20, 30)

# Solution 2
from fractions import gcd
print (gcd(20,30))