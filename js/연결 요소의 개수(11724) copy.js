const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const [n, m] = input[0].split(' ').map(Number);
const graph = Array.from({length:n+1}, () => []);
for (let i=1; i<m+1; i++) {
    const [a,b] = input[i].split(' ').map(Number);
    graph[a].push(b);
    graph[b].push(a);
}

const visited = Array.from({length:n+1}, () => 0);
let cnt = 0;

function dfs(x) {
    visited[x] = 1;
    for (let i of graph[x]) {
        if (visited[i] === 0) {
            visited[i] = 1;
            dfs(i);
        }
    }
}

for (let i=1; i<n+1; i++) {
    if (visited[i] === 0) {
        cnt++;
        dfs(i);
    }
}
console.log(cnt);