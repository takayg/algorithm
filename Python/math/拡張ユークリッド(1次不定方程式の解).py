# 再帰
# ax + by = gcd(a, b)
# return (gcd, x, y) (xが絶対値最小)
def egcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        g, y, x = egcd(b, (a % b))
        return g, x, y - (a // b) * x
    
print(egcd(5, 3))