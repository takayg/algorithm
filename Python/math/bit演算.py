x_and_y = x & y # 論理積
x_or_y = x | y # 論理和
x_xor_y = x ^ y # 排他的論理和

# bit全探索(bit演算ver)
n = 3
for i in range(1 << n):
    for j in range(n):
        if i & (1 << j):
            # 処理内容

# bit全探索(2進数ver)
n = 3
for i in range(2**n):
    i_bin = bin(i)[2:].zfill(n)
    for j in range(n):
        if i_bin[j]:
            # 処理内容