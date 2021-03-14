i = 3
bin_1 = bin(i) #プレフィックス付き2進数（0b11）
bin_1 = bin(i).zfill(4) # 0011
bin_2 = format(i, 'b') #プレフィックスなし2進数、（11）
bin_2 = format(i, '04b') #プレフィックスなし2進数、0埋め（0011）