def dfs(u):
    stack = [u]
    d = [None] * n
    d[u] = 0
    while stack:
        v = stack.pop()
        for i in g[v]:
            if d[i] is None:
                d[i] = d[v] + 1
                stack.append(i)
    return d

