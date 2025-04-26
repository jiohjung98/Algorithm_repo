// N x M 공간 - 아기 상어 존재
// 어떤 칸의 안전 거리 - 그 칸과 가장 거리가 가까운 아기 상어와의 거리
// 이동은 인접합 8방향(대각선 포함) 가능
// 안전 거리가 가장 큰 칸 구해라

// 입력
// 첫째 줄: N, M
// 둘째 줄 ~ N+1번째 줄 : 공간 상태
// 0 : 빈 칸, 1 : 아기 상어

// 0의 입장에서 대각선으로 이동하다가 1을 만나면 종료
// 이동할 때 마다 cnt++
// 종료할 때 cnt 배열에 넣고
// 마지막에 가장 큰 값 출력

const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const [N, M] = input[0].split(' ').map(Number);
const graph = input.slice(1, N+1).map((line => line.split(' ').map(Number)));

// const visited = Array.from({length:N}, () => Array(M).fill(false));

const dx = [-1,1,0,0,1,1,-1,-1];
const dy = [0,0,-1,1,1,-1,-1,1];

let cnt_list = [];

function bfs(x,y) {
    let  visited = Array.from({length:N}, () => Array(M).fill(false));
    let queue = [];
    queue.push([x,y,1]);
    visited[x][y] = true;

    while (queue.length) {
        const [x,y, dist] = queue.shift();

        for (let i=0; i<8; i++) {
            let nx = x + dx[i];
            let ny = y + dy[i];

            if (nx >= 0 && nx < N && ny >= 0 && ny < M && !visited[nx][ny]) {
                if (graph[nx][ny] === 1) {
                    cnt_list.push(dist);
                    return;
                }
                visited[nx][ny] = true;
                queue.push([nx,ny, dist+1]);
            }
        }
    }
}

for (let i=0; i<N; i++) {
    for (let j=0; j<M; j++) {
        if (graph[i][j] === 0) {
            bfs(i,j);
        }
    }
}

console.log(Math.max(...cnt_list));