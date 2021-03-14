"""
区間min更新、1点取得
update: 区間[l, r)をxと小さい方の値に変更する
query: i番目の値を求める
"""

def segfun(x, y):
    return min(x, y)
ide_ele = float("inf")


class SegmentTree:
    def __init__(self, n, ele, segfun):
        self.ide_ele = ele
        self.segfun = segfun
        self.n = n
        self.N0 = 1 << n.bit_length()
        self.data = [self.ide_ele] * (self.N0 * 2)
 
    def update(self, l, r, val):
        l += self.N0
        r += self.N0
        while l < r:
            if l & 1:
                self.data[l] = self.segfun(self.data[l], val)
                l += 1
            if r & 1:
                self.data[r - 1] = self.segfun(self.data[r - 1], val)
                r -= 1
            l //= 2
            r //= 2
 
    def query(self, i):
        i += len(self.data) // 2
        ret = self.data[i]
        while i > 0:
            i //= 2
            ret = self.segfun(ret, self.data[i])
        return ret
