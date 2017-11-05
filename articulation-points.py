import sys
from collections import defaultdict, deque

def _my_nx_dfs(adj, components=True):
    # depth-first search algorithm to generate articulation points and biconnected components
    visited = set()
    for start in sorted(adj.keys()):
        if start in visited:
            continue
        discovery = {start:0} # "time" of first discovery of node during search
        low = {start:0}
        root_children = 0
        visited.add(start)
        edge_stack = []
        stack = [(start, start, iter(adj[start]))]
        while stack:
            grandparent, parent, children = stack[-1]
            try:
                child = next(children)
                if grandparent == child:
                    continue
                if child in visited:
                    if discovery[child] <= discovery[parent]: # back edge
                        low[parent] = min(low[parent],discovery[child])
                        if components:
                            edge_stack.append((parent,child))
                else:
                    low[child] = discovery[child] = len(discovery)
                    visited.add(child)
                    stack.append((parent, child, iter(adj[child])))
                    if components:
                        edge_stack.append((parent,child))
            except StopIteration:
                stack.pop()
                if len(stack) > 1:
                    if low[parent] >= discovery[grandparent]:
                        if components:
                            ind = edge_stack.index((grandparent,parent))
                            yield edge_stack[ind:]
                            edge_stack=edge_stack[:ind]
                        else:
                            yield grandparent
                    low[grandparent] = min(low[parent], low[grandparent])
                elif stack: # length 1 so grandparent is root
                    root_children += 1
                    if components:
                        ind = edge_stack.index((grandparent,parent))
                        yield edge_stack[ind:]
        if not components:
            # root node is articulation point if it has more than 1 child
            if root_children > 1:
                yield start

def my_nx_articulation_points(edge_list):
    adj = defaultdict(set)
    for a,b in edge_list:
        adj[a].add(b)
        adj[b].add(a)
    if not adj:
        return []
    return sorted(set(_my_nx_dfs(adj, components=False)))

edge_list = list(tuple(map(int, s.split())) for s in sys.stdin)
#edge_list = test_edges
cuts = my_nx_articulation_points(edge_list)
print(' '.join(str(v) for v in cuts))
