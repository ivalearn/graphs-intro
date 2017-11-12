from sys import stdin
from collections import defaultdict
a = defaultdict(set)
for p, v in (map(int, s.split()) for s in stdin):
    a[p].add(v)
    a[v].add(p)
r = set()
k = {0: 0}
l = {0: 0}
n = 0
s = [(0, 0, iter(a[0]))]
while s:
    p, v, i = s[-1]
    for c in i:
        if c==p:  continue
        if c in k:
            if k[c] <= k[v]:
                l[v] = min(l[v], k[c])
        else:
            if not v:  n+=1
            l[c] = k[c] = len(k)
            s.append((v, c, iter(a[c])))
        break
    else:
        s.pop()
        if len(s) > 1:
            if l[v] >= k[p]:
                r.add(p)
            l[p] = min(l[v], l[p])
if n > 1:  r.add(0)
print(' '.join(str(s) for s in sorted(r)))
