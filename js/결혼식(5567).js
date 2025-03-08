const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const n = Number(input[0]);
const m = Number(input[1]);
const graph = Array.from({ length: n + 1 }, () => []);

for (let i = 2; i < 2 + m; i++) {
    const [a, b] = input[i].split(' ').map(Number);
    graph[a].push(b);
    graph[b].push(a);
}

const visited = Array(n + 1).fill(0);

function bfs(start) {
    const queue = [];
    queue.push(start);
    visited[start] = 1; 

    while (queue.length > 0) {
        const friendNum = queue.shift(); 

        for (const peopleNum of graph[friendNum]) {
            if (visited[peopleNum] === 0) { 
                queue.push(peopleNum);
                visited[peopleNum] = visited[friendNum] + 1;
            }
        }
    }
}

bfs(1); 

let result = 0;

for (let i = 2; i <= n; i++) {
    if (visited[i] > 0 && visited[i] <= 3) {
        result++;
    }
}

console.log(result);