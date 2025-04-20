// 치즈(2636)

const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const [n, m] = input[0].split(' ').map(Number);
const graph = input.slice(1, n+1).map((line) => line.split(' ').map(Number));

const dx = [-1,1,0,0];
const dy = [0,0,-1,1];

function bfs() {
    let visited = Array.from({length:n}, () => Array(m).fill(false));
    let queue = [];
    queue.push([0,0]);
    visited[0][0] = true;
    let melt = [];

    while (queue.length) {
        const [x,y] = queue.shift();

        for (let i=0; i<4; i++) {
            let nx = x + dx[i];
            let ny = y + dy[i];

            if (nx >=0 && nx < n && ny >=0 && ny < m && !visited[nx][ny]) {
                visited[nx][ny] = true;

                if (graph[nx][ny] === 0) {
                    queue.push([nx,ny]);
                }
                else if (graph[nx][ny] === 1) {
                    melt.push([nx,ny]);
                }
            }
        }
    }
    return melt;
}

let total_time = 0;
let last_cheese_cnt = 0;

while (true) {
    let melt_list = bfs();

    if (melt_list.length === 0) break;

    for (const [x, y] of melt_list) {
        graph[x][y] = 0;
    }

    last_cheese_cnt = melt_list.length;

    total_time++;
}

console.log(total_time);
console.log(last_cheese_cnt);