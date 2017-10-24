'use strict';

let stdin = '';
process.stdin.on('data', buf => stdin += String(buf));
process.stdin.on('end', _ => {
    let pairs = stdin.trim().split(/[\r\n]+/).map(s => s.trim().split(/\s+/));
    let [nv, ne] = pairs.shift();
    let verts = Array.from(Array(+nv), _ => ({}));
    for (let [a,b] of pairs)
        verts[a-1][b-1] = verts[b-1][a-1] = true;
    console.log(count_comps(verts));
    process.exit(0);
});

function count_comps(verts) {
    let nc = 0;
    let visited = new Array(verts.length);
    visited.fill(false);
    while (1) {
        const next = visited.indexOf(false);
        if (next === -1)
            return nc;
        ++nc;
        dfs(next);
    }

    function dfs(v) {
        visited[v] = true;
        for (let w in verts[v])
            if (!visited[w])
                dfs(w);
    }
}
