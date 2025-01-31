const input = require('fs').readFileSync('dev/stdin').toString().trim().split('\n');

const N = +input.shift();
const M = +input.shift();

const graph = Array.from(Array(N+1), () => []);
const visited = Array.from(Array(N+1), () => false);
visited[1] = true;
let cnt = 0;

for (let i=0; i<M; i++) {
    const [first, second] = input[i].split(" ").map(Number);
    graph[first].push(second);
    graph[second].push(first);
}

function dfs(v) {
    for (let i of graph[v]) {
        if (visited[i] === false) {
            visited[i] = true;
            cnt++;
            dfs(i);
        }
    }
}

dfs(1);
console.log(cnt);