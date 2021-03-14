class DualSegmentTree():
    """区間更新、一点取得クエリをそれぞれO(logN)で答えるデータ構造を構築する
    update: 区間[l, r)をxに変更する
    get_x: i番目の値を求める
    """
    def __init__(self, n):
        self.update_cnt = 0
        self.n = n
        self.size = 1
        INF = 2**31 - 1
        while self.size < n:
            self.size *= 2
        self.node = [[self.update_cnt, INF] for i in range(2*self.size - 1)]

    def update(self, l, r, x):
        self.update_cnt += 1
        l += (self.size - 1)
        r += (self.size - 1)
        while l < r:
            if (r - 1) & 1:
                r -= 1
                self.node[r] = [self.update_cnt, x]
            if (l - 1) & 1:
                self.node[l] = [self.update_cnt, x]
                l += 1
            l = (l - 1) // 2
            r = (r - 1) // 2

    def get_x(self, i):
        i += (self.size - 1)
        x = self.node[i]
        while i > 0:
            i = (i - 1) // 2
            x = max(x, self.node[i])
        return x[1]

