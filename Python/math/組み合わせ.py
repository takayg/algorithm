#組み合わせ（modで割ったあまり）
def nCk(n, k, mod=10 ** 9 + 7):
    if n < k:
        return 0
    k = min(k, n - k)
    numer = 1
    for x in range(n - k + 1, n + 1):
        numer = (numer * x) % mod
    denom = 1
    for x in range(1, k + 1):
        denom = (denom * x) % mod
    return numer * pow(denom, mod - 2, mod) % mod
X = 999999
Y = 999999
n = (2*Y - X)//3
m = (2*X - Y)//3
print(nCk(n+m,m))