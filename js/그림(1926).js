const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const [n, m] = input[0].split(' ').map(Number);
const graph = [];
const visited = Array.from({length: n}, () => Array(m).fill(false));

for (let i=1; i<=n; i++) {
    const row = input[i].split(' ').map(Number);
    graph.push(row);
}

const dx = [-1,1,0,0];
const dy = [0,0,-1,1];
const extent_arr = [];

function bfs(x,y) {
    const queue = [];
    queue.push([x,y]);
    visited[x][y] = true;
    let extent = 1;

    while (queue.length) {
        const [x,y] = queue.shift();

        for (let i=0; i<4; i++) {
            const nx = x + dx[i];
            const ny = y + dy[i];

            if (nx >= 0 && nx < n && ny >= 0 && ny < m && !visited[nx][ny] && graph[nx][ny] === 1) {
                visited[nx][ny] = true;
                graph[nx][ny] = graph[x][y] + 1;
                queue.push([nx,ny]);
                extent++;
            }
        }
    }
    extent_arr.push(extent);
}

let cnt = 0;
for (let i=0; i<n; i++) {
    for (let j=0; j<m; j++) {
        if (graph[i][j] === 1) {
            bfs(i,j);
            cnt++;
        }
    }
}

if (extent_arr.length > 0) {
    console.log(cnt);
    console.log(Math.max(...extent_arr));
} else {
    console.log(0);
    console.log(0);
}