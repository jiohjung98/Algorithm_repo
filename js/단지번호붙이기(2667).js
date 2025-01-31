const input = require('fs').readFileSync('/dev/stdin').toString().split('\n');

const N = +input.shift();
const arr = input.slice(0, N).map((line) => line.split("").map(Number));

const dx = [-1, 1, 0, 0];
const dy = [0, 0, -1, 1];
const answer = [];
let cnt = 0;

function bfs(x,y) {
    const queue = [];
    queue.push([x,y]);
    arr[x][y] = 0;
    cnt = 1

    while (queue.length) {
        const [x, y] = queue.shift();

        for (let i=0; i<4; i++) {
            const nx = x + dx[i];
            const ny = y + dy[i];

            if (nx < 0 || nx >= N || ny < 0 || ny >= N) {
                continue;
            } 
            if (arr[nx][ny] === 0) {
                continue;
            }

            if (arr[nx][ny] === 1) {
                arr[nx][ny] = 0;
                cnt++;
                queue.push([nx, ny]);
            }
        }
    }
    answer.push(cnt);
}

for (let i=0; i < N; i++) {
    for (let j=0; j < N; j++) {
        if (arr[i][j] === 1) {
            bfs(i,j);
        }
    }
}

console.log(answer.length);
answer.sort((a,b) => a-b);
answer.forEach((e) => console.log(e));