const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const n = Number(input[0]);
const m = Number(input[1]);
const graph = Array.from({length: n+1}, () => []);

for (let i=2; i<m+2; i++) {
    const [x,y] = input[i].split(' ').map(Number);
    graph[x].push(y);
    graph[y].push(x);
}

const visited = Array.from({length: n+1}, () => false);

function bfs(v) {
    const queue = [];
    queue.push(v);
    visited[v] = true;

    let cnt = 0;

    while (queue.length) {
        let a = queue.shift();
        for (let i of graph[a]) {
            if (!visited[i]) {
                visited[i] = true;
                cnt++;
                queue.push(i);
            }
        }
    }
    console.log(cnt);
}

bfs(1);