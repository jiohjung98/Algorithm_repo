const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const [N, M] = input[0].split(' ').map(Number);
const graph = Array.from({length: N+1}, () => []);
for (let i=0; i < M; i++) {
    const [a, b] = input[i+1].split(' ').map(Number);
    graph[a].push(b);
    graph[b].push(a);
}

const visited = Array.from({length: N+1}, () => false);

function dfs(v) {
    visited[v] = true;
    for (let i of graph[v]) {
        if (visited[i] === false) {
            visited[i] = true;
            dfs(i);
        }
    }
}

let cnt = 0;

for (let i=1; i <= N; i++) {
    if (visited[i] === false) {
        cnt++;
        dfs(i);
    } 
}

console.log(cnt);