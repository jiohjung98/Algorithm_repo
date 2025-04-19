// # 그림의 개수, 그림 중 가장 넓은 것의 너비 구하기 문제
// # 그림 : 1로 연결된 것을 한 그림이라고 정의
// # 가로, 세로로 연결된 것: 연결된 그림
// # 대각선으로 연결된 것: 떨어진 그림
// # 그림의 넓이 : 그림에 포함된 1의 개수

// # 입력: 세로 크기 n, 가로 크기 m
// # 두번째 줄 ~ n+1번째 줄: 그림 정보

const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const [n, m] = input[0].split(' ').map(Number);

const graph = input.slice(1, n+1).map((line) => line.split(' ').map(Number));
const visited = Array.from({length: n}, () => Array(m).fill(false));

const dx = [-1,1,0,0];
const dy = [0,0,-1,1];

const width_list = [];

function bfs(x,y) {
    let queue = [];
    queue.push([x,y]);
    let width = 1;

    while (queue.length) {
        const [x,y] = queue.shift();
        visited[x][y] = true;

        for (let i=0; i<4; i++) {
            let nx = x + dx[i];
            let ny = y + dy[i];

            if (nx >=0 && nx < n && ny >=0 && ny < m && !visited[nx][ny] && graph[nx][ny] === 1) {
                visited[nx][ny] = true;
                queue.push([nx,ny]);
                width++;
            }
        }
    }
    width_list.push(width);
}

for (let i=0; i<n; i++) {
    for (let j=0; j<m; j++) {
        if (!visited[i][j] && graph[i][j] === 1) {
            bfs(i,j);
        }
    }
}

if (width_list.length > 0) {
    console.log(width_list.length);
    console.log(Math.max(...width_list));
} else {
    console.log(0);
    console.log(0);
}