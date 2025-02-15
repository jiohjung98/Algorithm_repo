const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const [n, m] = input[0].split(' ').map(Number);
const [startX, startY, startDir] = input[1].split(' ').map(Number);

const arr = [];
for (let i=2; i<=n+1; i++) {
    arr.push(input[i].split(' ').map(Number));
}

const visited = Array.from({length:n}, () => Array(m).fill(0));

// 북, 동, 남, 서 방향
const dx = [-1, 0, 1, 0];
const dy = [0, 1, 0, -1];

let cnt = 0;

function bfs(x,y,d) {
    const queue = [];
    queue.push([x,y]);
    visited[x][y] = 2;
    cnt += 1;

    let index = 0;
    while (index < queue.length) {
        const [x, y] = queue[index++];
        let canGo = 0;

        for (let i=0; i<4; i++) {
            d = (d+3) % 4;
            let nx = x + dx[d];
            let ny = y + dy[d];

            if (nx >= 0 && nx < n && ny >= 0 && ny < m && visited[nx][ny] !== 2 && arr[nx][ny] !== 1) {
                visited[nx][ny] = 2;
                queue.push([nx,ny]);
                cnt += 1;
                canGo = 1;
                break;
            }
        }

        if (canGo === 0) {
            if (arr[x-dx[d]][y-dy[d]] !== 1) {
                queue.push([x-dx[d], y-dy[d]]);
            } else {
                console.log(cnt);
                break;
            }
        }   
    }
}

bfs(startX, startY, startDir);