nv, ne = map(int, input().split())
adj = [[] for _ in range(nv)]
for _ in range(ne):
    a, b = map(int, input().split())
    adj[a-1].append(b-1)
    adj[b-1].append(a-1)
visited = [False] * nv
stack = [None] * nv
nc = 0
for i in range(nv):
    if not visited[i]:
        nc += 1
        stack[0] = i
        ns = 1
        while ns:
            ns -= 1
            v = stack[ns]
            for w in adj[v]:
                if not visited[w]:
                    visited[w] = True
                    stack[ns] = w
                    ns += 1
print(nc)
