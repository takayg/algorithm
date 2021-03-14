# 複数の最小公倍数
import math
from functools import reduce

def lcm_base(x, y):
    return (x * y) // math.gcd(x, y)
    
def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)

print(lcm_list([27, 9, 3]))
# 27