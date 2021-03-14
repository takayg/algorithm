N = int(input())

def dec_to_n(N, n):
    if N == 0:
        return "0"
    digits = []
    base = 1
    while N != 0:
        if N % (base * n) == 0:
            digits.append('0')
        else:
            digits.append('1')
            N -= base
        base *= n
    return "".join(digits[::-1])

print(dec_to_n(N, -2))