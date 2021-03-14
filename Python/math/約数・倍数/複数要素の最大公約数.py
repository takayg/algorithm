#複数個の最大公約数
import math
from functools import reduce

def gcd(*numbers):
    return abs(reduce(math.gcd, numbers))

x = [-4, -2, 0]
print(gcd(*x))