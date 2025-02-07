const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
const n = Number(input[0]);
const [a, b] = input[1].split(' ').map(Number);
const m = Number(input[2]);

const visited = Array.from({length: n+1}, () => false);
const graph = Array.from({length: n+1}, () => []);

for (let i=0; i<m; i++) {
    const [x, y] = input[i+3].split(' ').map(Number);
    graph[x].push(y);
    graph[y].push(x);
}


function dfs(current, target, cnt) {
    visited[current] = true;

    if (current === target) {
        console.log(cnt);
        process.exit();
    }

    else {
        for (let neighbor of graph[current]) {
            if (!visited[neighbor]) {
                dfs(neighbor, target, cnt+1);
            }
        }
    }
}

dfs(a, b, 0);
console.log(-1);