const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const n = Number(input[0]);
const graph = input.slice(1, n+1).map((line) => line.split('').map(Number));
const visited = Array.from({length:n}, () => Array(n).fill(false));

// 상, 하, 좌, 우
const dx = [-1, 1, 0, 0];
const dy = [0, 0, -1, 1];

let cnt_list = [];

function bfs(x,y) {
    queue = [];
    queue.push([x,y]);
    visited[x][y] = true;
    let cnt = 1;

    while (queue.length) {
        const [x,y] = queue.shift();
        for (let i=0; i<4; i++) {
            let nx = x + dx[i];
            let ny = y + dy[i];

            if (nx >=0 && nx < n && ny >=0 && ny < n && !visited[nx][ny] && graph[nx][ny] === 1) {
                cnt++;
                visited[nx][ny] = true;
                queue.push([nx,ny]);
            }
        }
    }
    cnt_list.push(cnt);
}

let total_cnt = 0;

for (let i=0; i<n; i++) {
    for (let j=0; j<n; j++) {
        if (!visited[i][j] && graph[i][j] === 1) {
            bfs(i,j);
            total_cnt++;
        }
    }
}

cnt_list.sort((a,b) => a-b);
console.log(total_cnt);
for (let elem of cnt_list) {
    console.log(elem);
}