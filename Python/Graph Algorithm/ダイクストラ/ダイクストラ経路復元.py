import sys
input = sys.stdin.readline

import heapq
def dijkstra(s):
    # 始点から各頂点への最短距離
    d = [float('inf')]*n
    d[s] = 0
    # 各頂点が訪問済みかどうか
    used = [False]*n
    used[s] = True
    # 仮の距離を記録するヒープ
    que = []
    for e in g[s]:
        heapq.heappush(que, e)
    while que:
        u, v, p = heapq.heappop(que)
        if used[v]:
            continue
        d[v] = u
        used[v] = True
        parent[v] = p
        for e in g[v]:
            if not used[e[1]]:
                heapq.heappush(que, [e[0] + d[v], e[1], v])
    return d
##############################################
# n:頂点数 m:辺数 s:スタート t:ゴール
n, m, s, t = [int(x) for x in input().split()]
g = [[] for _ in range(n)]
parent = [-1]*n
for _ in range(m):
    a, b, c = [int(x) for x in input().split()]
    g[a].append([c, b, a])
d = dijkstra(s)
if d[t] == float("inf"):
    print(-1)
    sys.exit()
ans = []
start = t
while True:
    ans.append([parent[start], start])
    if parent[start] == s:
        break
    start = parent[start]
print(d[t], len(ans))
for i in ans[::-1]:
    print(*i)