nv, ne = map(int, input().split())

verts = [[] for _ in range(nv)]
for _ in range(ne):
    a, b = map(int, input().split())
    verts[a-1].append(b-1)
    verts[b-1].append(a-1)

visited = [False] * nv
nc = 0
        
def dfs(v):
    visited[v] = True
    for w in verts[v]:
        if not visited[w]:
            dfs(w)

for v in range(len(visited)):
    if not visited[v]:
        nc += 1
        dfs(v)
   
print(nc)