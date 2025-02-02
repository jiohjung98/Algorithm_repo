const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const [M, N, K] = input[0].split(' ').map(Number);
const arr = Array.from({ length: M }, () => Array(N).fill(0));
const size_arr = [];
var cnt = 0;
const dx = [-1,1,0,0];
const dy = [0,0,-1,1];


for (let i=0; i<K; i++) {
    const [startX, startY, endX, endY] = input[i+1].split(' ').map(Number);

    for (let x=startX; x<endX; x++) {
        for (let y=startY; y<endY; y++) {
            arr[y][x] = -1;
        }
    }
}

function bfs(x,y) {
    const queue = [];
    queue.push([x,y]);
    arr[x][y] = 1;
    let size = 1;

    while (queue.length) {
        const [x,y] = queue.shift();

        for (let i=0; i < 4; i++) {
            const nx = x + dx[i];
            const ny = y + dy[i];

            if (nx < 0 || nx >= M || ny < 0 || ny >= N) {
                continue;
            }
            if (arr[nx][ny] == 0) {
                arr[nx][ny] = 1;
                size++;
                queue.push([nx,ny]);
            }
        }
    }
    size_arr.push(size);
}

for (let i=0; i < M; i++) {
    for (let j=0; j < N; j++) {
        if (arr[i][j] == 0) {
            bfs(i,j);
            cnt++;
        }
    }
}

console.log(cnt);
size_arr.sort((a,b) => a-b);
console.log(size_arr.join(' '));