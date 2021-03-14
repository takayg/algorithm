prev = [-1]*n
from collections import deque
def bfs(v):
    queue = deque([v])
    d = [None]*n
    d[v] = 0
    while queue:
        u = queue.popleft()
        for i in g[u]:
            if d[i] is None:
                d[i] = d[u] + 1
                prev[i] = u
                queue.append(i)
    return d