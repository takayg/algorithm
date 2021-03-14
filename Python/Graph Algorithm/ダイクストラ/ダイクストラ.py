# O(ElogV)
import heapq
def dijkstra(s):
    # 始点sから各頂点への最短距離
    d = [float('inf')]*n
    d[s] = 0
    # 各頂点が訪問済みかどうか
    used = [False]*n
    used[s] = True
    # 仮の距離を記録するヒープ
    que = []
    for e in edge[s]:
        heapq.heappush(que, e)
    while que:
        minedge = heapq.heappop(que)
        if used[minedge[1]]:
            continue
        v = minedge[1]
        d[v] = minedge[0]
        used[v] = True
        for e in edge[v]:
            if not used[e[1]]:
                heapq.heappush(que, [e[0] + d[v], e[1]])
    return d
##############################
n, w = [int(x) for x in input().split()] # n:頂点数 w:辺の数
edge = [[] for _ in range(n)]
# edge[i]:iから出る辺の[コスト,行先]
for _ in range(w):
    x, y, z = [int(x) for x in input().split()]
    edge[x].append([z, y])
    edge[y].append([z, x])
print(dijkstra(0))