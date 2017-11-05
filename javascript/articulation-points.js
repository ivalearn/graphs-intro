'use strict';

if (false) {
    let stdin = '';
    process.stdin.on('data', buf => stdin += String(buf));
    process.stdin.on('end', _ => {
        let edge_list = stdin.trim().split(/[\r\n]+/).map(s => s.trim().split(/\s+/));
        let cut_points = articulation_points(edge_list);
        console.log(cut_points.join(' '));
        process.exit(0);
    });
} else {
    let stdin = '0 1\n1 2\n2 0\n3 2\n4 3\n4 2\n5 4\n';
    let edge_list = stdin.trim().split(/[\r\n]+/).map(s => s.trim().split(/\s+/));
    let cut_points = articulation_points(edge_list);
    console.log(cut_points.join(' '));
    process.exit(0);
}

function articulation_points(edge_list) {
    if (edge_list.length == 0)
        return [];
    let nv = Math.max(...edge_list.map(e => Math.max(...e))) + 1;

    let adj = Array.from(Array(nv), _ => ({}));
    for (let [a, b] of edge_list) {
        adj[a][b] = adj[b][a] = true;
    }

    if (adj.length !== nv)
        throw "Non-continuous edges!";

    let edges = {};

    let visited = new Array(nv);  visited.fill(false);
    let k_val = new Array(nv);  k_val.fill(null);
    let parents = new Array(nv);  parents.fill(null);
    let l_val = new Array(nv);  l_val.fill(null);
    let l_children = new Array(nv);  l_children.fill(0);
    let n_children = new Array(nv);  n_children.fill(0);

    let nodes = Object.keys(adj);  nodes.sort();
    let todo1 = adj.map(a => Object.keys(a).map(u => +u));
    let todo2 = adj.map(_ => []);
    let stack = [0];
    let k_no = 1;
    let u, v;

    k_val[0] = l_val[0] = 1;
    visited[0] = true;

    while (stack.length) {
        v = stack[stack.length - 1];
        if (todo2[v].length) {
            u = todo2[v].pop();
            if (l_val[u] < l_val[v])
                l_val[v] = l_val[u];
            if (l_val[u] > l_children[v])
                l_children[v] = l_val[u];
        } else if (todo1[v].length) {
            u = todo1[v].pop();
            if (visited[u])
                continue;
            parents[u] = v;
            edges[v + ',' + u] = edges[u + ',' + v] = true;
            n_children[v] += 1;
            visited[u] = true;
            k_no++;
            k_val[u] = l_val[u] = k_no;
            todo2[v].push(u);
            stack.push(u);
        } else {
            v = stack.pop();
            u = parents[v];
            while (u !== null) {
                if ((u in adj[v]) && (k_val[u] < l_val[v]) && !((u + ',' + v) in edges))
                    l_val[v] = k_val[u];
                u = parents[u];
            }
        }
    }
    let cuts = [];
    for (let v of nodes) {
        if ((v === 0 && n_children[v] > 1) || (v > 0 && l_children[v] >= k_val[v]))
            cuts.push(v);
    }
    cuts.sort();
    return cuts;
}
