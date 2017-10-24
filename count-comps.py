nv, ne = (int(x) for x in input().split())

verts = [set() for _ in range(nv)]
for _ in range(ne):
    a,b = (int(x) for x in input().split())
    verts[a-1].add(b-1)
    verts[b-1].add(a-1)

def dfs(v):
    visited[v] = True
    for w in verts[v]:
        if not visited[w]:
            dfs(w)

visited = [False] * nv
nc = 0
while 1:
    try:
        i = visited.index(False)
    except ValueError:
        break
    nc += 1
    dfs(i)

print(nc)
