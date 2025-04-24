// # 콘도미니엄 8층 : 학생들이 3끼 식사 해결하는 공간
// # 몇몇 학생들 때문에 음식물이 통로 중간중간 떨어져있음
// # 음식물 근처에 있는 것들이 뭉침 -> 큰 음식물 쓰레기 탄생
// # 통로에 떨어진 음식물 피하기가 어려움
// # 떨어진 음식물들 중에 제일 큰 음식물을 피하고자 함

// # 입력
// # 첫째 줄 : 세로 N, 가로 M, 음식물 쓰레기 개수 K
// # 둘째 줄 ~ K+1줄 : 음식물 떨어져있는 좌표(r,c)

// # 출력
// # 가장 큰 음식물 크기

const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const [N, M, K] = input[0].split(' ').map(Number);
const graph = Array.from({length:N}, () => Array(M).fill(0));
const visited =  Array.from({length:N}, () => Array(M).fill(false));

for (let i=1; i<=K; i++) {
    let [x,y] = input[i].split(' ').map(Number);
    graph[x-1][y-1] = 1;
}

const dx = [-1,1,0,0];
const dy = [0,0,-1,1];
let cnt_list = [];

function bfs(x,y) {
    let queue = [];
    queue.push([x,y]);
    visited[x][y] = true;
    let cnt = 1;

    while (queue.length) {
        const [x,y] = queue.shift();
        for (let i=0; i<4; i++) {
            let nx = x + dx[i];
            let ny = y + dy[i];

            if (nx >= 0 && nx < N && ny >= 0 && ny < M && !visited[nx][ny] && graph[nx][ny] === 1) {
                visited[nx][ny] = true;
                queue.push([nx,ny]);
                cnt++;
            }
        }
    }
    cnt_list.push(cnt);
}

for (let i=0; i<N; i++) {
    for (let j=0; j<M; j++) {
        if (graph[i][j] === 1) {
            bfs(i,j);
        }
    }
}

console.log(Math.max(...cnt_list));