const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const [n, m] = input[0].split(' ').map(Number);
const graph = input.slice(1).map(line => line.split(' ').map(Number));
const dx = [-1,1,0,0];
const dy = [0,0,-1,1];
var answer = [];

function bfs() {
    const queue = [];
    // 깊은 복사
    const tmpGraph = graph.map(row => [...row]);

    for (let i=0; i < n; i++) {
        for (let j=0; j < m; j++) {
            if (tmpGraph[i][j] === 2) {
                queue.push([i,j]);
            }
        }
    }

    while (queue.length) {
        const [x, y] = queue.shift();

        for (let i=0; i<4; i++) {
            const nx = x + dx[i];
            const ny = y + dy[i];

            if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
            if (tmpGraph[nx][ny] === 0) {
                tmpGraph[nx][ny] = 2;
                queue.push([nx,ny]);
            }
        }
    }

    const cntZero = tmpGraph.flat().reduce((count,num) => count + (num === 0 ? 1 : 0), 0);
    answer.push(cntZero);
}

function makeWall(cnt) {
    if (cnt === 3) {
        bfs();
        return;
    }

    for (let i=0; i<n; i++) {
        for (let j=0; j<m; j++) {
            if (graph[i][j] === 0) {
                graph[i][j] = 1;
                makeWall(cnt+1);
                graph[i][j] = 0;
            }
        }
    }
}

makeWall(0);
console.log(Math.max(...answer));