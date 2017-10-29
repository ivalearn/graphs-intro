def fast_eulerian_circuit(nv, edges):
    adj = [[] for i in range(nv)]
    for a,b in edges:
        adj[a].append(b)
        adj[b].append(a)
    for v in range(nv):
        adj[v].sort()

    if any(not(a) or len(a) % 2 == 1 for a in adj):
        return None  # not eulerian

    ca = []
    while True:
        for s in (ca or range(nv)):
            if adj[s]:
                break
        else:
            break

        cc = [s]
        v = s
        while adj[v]:
            w = adj[v][0]
            adj[v].remove(w)
            adj[w].remove(v)
            cc.append(w)
            v = w

        assert cc[0] == cc[-1]
        if ca:
            i = ca.index(s)
            ca[i:i+1] = cc
        else:
            ca.extend(cc)

    if any(a for a in adj):
        return None

    assert ca[0] == ca[-1]
    return ca[:-1]

nv, ne = map(int, input().split())
edges = [(a-1,b-1) for a,b in (map(int, input().split()) for _ in range(ne))]
circuit = fast_eulerian_circuit(nv, edges)
if circuit is None:
    print('NONE')
else:
    print(' '.join(str(v+1) for v in circuit))
