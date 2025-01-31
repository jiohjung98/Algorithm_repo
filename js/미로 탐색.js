let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');

const [n, m] = input[0].split(' ').map(Number);
const arr = input.slice(1, n+1).map((line) => line.split("").map(Number));

const visited = Array.from({length: n}, () => Array(m).fill(false));

const dx = [-1, 1, 0, 0];
const dy = [0, 0, -1, 1];

function bfs(x,y) {
    const queue = [[x,y]];
    visited[x][y] = true;

    while (queue.length) {
        const [x, y] = queue.shift();

        for (let i=0; i<4; i++) {
            const nx = x + dx[i]
            const ny = y + dy[i]

            if (nx >= 0 && nx < n && ny >= 0 && ny < m) {
                if (arr[nx][ny] === 1 && !visited[nx][ny]) {
                    arr[nx][ny] = arr[x][y] + 1;
                    queue.push([nx, ny]);
                    visited[nx][ny] = true;
                }
            }
        }
    }
}

bfs(0,0);
console.log(arr[n-1][m-1]);