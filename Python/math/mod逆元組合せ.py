n, k = [int(x) for x in input().split()]

def make_tables(n, mod = 10 ** 9 + 7):
    fac = [1, 1] # 階乗テーブル
    finv = [1, 1] #逆元の階乗テーブル
    inv = [0, 1] #逆元テーブル

    for i in range(2, n + 1):
        fac.append((fac[-1] * i) % mod)
        inv.append((mod -inv[mod % i] * (mod // i)) % mod)
        finv.append((finv[-1] * inv[-1]) % mod)
    return fac, finv

def nCk(n, k, mod = 10 ** 9 + 7):
    k = min(k, n-k)
    return fac[n] * finv[k] * finv[n-k] % mod

##########################
fac, finv = make_tables(n)
ans = nCk(n, k)

print(ans)