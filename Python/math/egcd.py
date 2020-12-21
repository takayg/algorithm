# 再帰
# ax + by = gcd(a, b)
def egcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        g, y, x = egcd(b, (a % b))
        return g, x, y - (a // b) * x