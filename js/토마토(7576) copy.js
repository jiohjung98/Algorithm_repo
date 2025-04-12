const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const [m, n] = input[0].split(' ').map(Number);
const graph = input.slice(1).map((line) => line.split(' ').map(Number));

const dx = [-1,1,0,0];
const dy = [0,0,-1,1];
let queue = [];

for (let i=0; i<n; i++) {
    for (let j=0; j<m; j++) {
        if (graph[i][j] === 1) {
            queue.push([i,j]);
        }
    }
}

let front = 0;

function bfs() {
    while (front < queue.length) {
        const [x, y] = queue[front];
        front++;

        for (let i=0; i<4; i++) {
            const nx = x + dx[i];
            const ny = y + dy[i];

            if (nx >=0 && nx < n && ny >=0 && ny < m && graph[nx][ny] === 0) {
                graph[nx][ny] = graph[x][y] + 1;
                queue.push([nx,ny]);
            }
        }
    }
}

bfs();

let ans = 0;

for (let g of graph) {
    for (let elem of g) {
        if (elem === 0) {
            console.log(-1);
            return;
        }
    }
    ans = Math.max(ans, Math.max(...g));
}

console.log(ans-1);