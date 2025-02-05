const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const N = Number(input[0]);

const graph = Array.from({ length: N + 1 }, () => []);
const visited = Array(N + 1).fill(false);
const parent = Array(N + 1).fill(0);

for (let i = 1; i < N; i++) {
    const [s, e] = input[i].split(' ').map(Number);
    graph[s].push(e);
    graph[e].push(s);
}

function dfs(v) {
    visited[v] = true;
    for (let i of graph[v]) {
        if (!visited[i]) {
            parent[i] = v;
            dfs(i);
        }
    }
}

dfs(1);

// ✅ `parent[2]`부터 출력해야 함
console.log(parent.slice(2).join("\n"));