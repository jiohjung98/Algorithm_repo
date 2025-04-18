// # 치즈 심화문제
// # N : 세로 격자 수
// # M : 가로 격자 수
// # 공기 : 0, 치즈 : 1
// # 치즈의 사방면 중 2곳 이상이 공기와 접촉 -> 한시간만에 녹음
// # 치즈로 둘러쌓인 공기 -> 효력없음

const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const [n, m] = input[0].split(' ').map(Number);
const graph = input.slice(1, n+1).map((line) => line.split(' ').map(Number));

const dx = [-1,1,0,0];
const dy = [0,0,-1,1];

function bfs() {
    const visited = Array.from({length:n}, () => Array(m).fill(false));
    let queue = [];
    queue.push([0,0]);
    visited[0][0] = true;
    let melt = [];

    while (queue.length) {
        const [x,y] = queue.shift();

        for (let i=0; i<4; i++) {
            let nx = x + dx[i];
            let ny = y + dy[i];

            if (nx >= 0 && nx < n && ny >= 0 && ny < m && !visited[nx][ny]) {
                if (graph[nx][ny] === 0) {
                    queue.push([nx,ny]);
                    visited[nx][ny] = true;
                }
                else if (graph[nx][ny] === 1) {
                    let cnt = 0
                    for (let j=0; j<4; j++) {
                        let kx = nx + dx[j];
                        let ky = ny + dy[j];

                        if (kx >= 0 && kx < n && ky >= 0 && ky < m && visited[kx][ky] && graph[kx][ky] === 0) {
                            cnt += 1;
                        }
                    }
                    if (cnt >= 2) {
                        melt.push([nx,ny]);
                    }
                }
            }
        }
    }
    return melt;
}

let total_time = 0;
while (true) {
    let melt_list = bfs();

    if (melt_list.length === 0) break;

    for (const [x,y] of melt_list) {
        graph[x][y] = 0;
    }
    total_time += 1;
}

console.log(total_time);