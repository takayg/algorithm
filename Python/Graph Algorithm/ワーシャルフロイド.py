"""
ワーシャルフロイド法:O(n^3)
n:頂点数
"""
def warshall_floyd(d):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d

#######################
inf = float('inf')
n, w = [int(x) for x in input().split()] # n:頂点数, w:辺数
d = [[inf]*n for _ in range(n)]
for i in range(n):
    d[i][i] = 0
for _ in range(w):
    x, y, z = [int(x) for x in input().split()] # 頂点xと頂点yの間の距離がz
    d[x][y] = z
    d[y][x] = z # 有向グラフならこの行はコメントアウト
d = warshall_floyd(d)

# 負の閉路検出
for i in range(n):
    if d[i][i] < 0:
        print("NEGATIVE CYCLE")
        exit()
for i in d:
    print(" ".join([str(x) for x in i]).replace("inf", "INF"))
