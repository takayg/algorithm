def dec_to_n(N, n):
    if N == 0:
        return "0"
    digits = []
    base = 1
    while N != 0:
        if N % (base * n) == 0:
            digits.append('0')
        else:
            digits.append(str(N % (base * n) // base))
            N -= N % (base * n)
        base *= n
    return "".join(digits[::-1])