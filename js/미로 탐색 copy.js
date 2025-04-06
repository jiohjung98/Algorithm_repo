const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const [n, m] = input[0].split(' ').map(Number);
const graph = input.slice(1, n+1).map(line => line.split("").map(Number));

// 상, 하, 좌, 우
const dx = [-1,1,0,0];
const dy = [0,0,-1,1];

function bfs(x,y) {
    queue = [];
    queue.push([x,y]);

    while (queue.length) {
        const [x,y] = queue.shift();

        for (let i=0; i<4; i++) {
            const nx = x + dx[i];
            const ny = y + dy[i];

            if (nx >= 0 && nx < n && ny >=0 && ny < m && graph[nx][ny] === 1) {
                graph[nx][ny] = graph[x][y] + 1;
                queue.push([nx,ny]);
            }
        }
    }

    console.log(graph[n-1][m-1]);
}

bfs(0,0);