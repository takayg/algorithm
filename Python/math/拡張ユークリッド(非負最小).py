# ax + by = z
# return (z, a, b, u, v) (a, b >= 0 && aが最小)

def ex_euclid(x, y):
    c0, c1 = x, y
    a0, a1 = 1, 0
    b0, b1 = 0, 1
 
    while c1 != 0:
        m = c0 % c1
        q = c0 // c1
 
        c0, c1 = c1, m
        a0, a1 = a1, (a0 - q * a1)
        b0, b1 = b1, (b0 - q * b1)
 
    return c0, a0, b0

def exex_euclid(x,y,z):
    c, a, b = ex_euclid(x, y)
    w, m = divmod(z, c)
     
    # zがcの倍数でないなら等式は不可能
    if m != 0:
        return None
         
    u, v = x // c, y // c
    a, b = a * w, b * w
 
    # aを非負数の中で最小にする
    f, a = divmod(a, v)
    b += u * f
     
    # aを最小にしたのにbが負なら、ともに正の組は不可能
    if b < 0:
        return None
    return c, a, b, u, v
 