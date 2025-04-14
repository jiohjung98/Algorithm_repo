const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const n = Number(input[0]);
const graph = input.slice(1).map((line) => line.split('').map(Number));

let visited = Array.from({length:n}, () => Array(n).fill(0));

const dx = [-1, 1, 0, 0];
const dy = [0, 0, -1, 1];

function bfs(x,y) {
    let queue = [];
    queue.push([x,y]);
    visited[x][y] = 1;

    let front = 0;

    while (front < queue.length) {
        const [x,y] = queue[front];
        front++;

        for (let i=0; i<4; i++) {
            let nx = x + dx[i];
            let ny = y + dy[i];

            if (nx >= 0 && nx < n && ny >= 0 && ny < n && visited[nx][ny] === 0 && graph[x][y] === graph[nx][ny]) {
                queue.push([nx,ny]);
                visited[nx][ny] = 1;
            }
        }
    }
}

// 적록색약이 아닌 사람부터
let cnt1 = 0;
for (let i=0; i<n; i++) {
    for (let j=0; j<n; j++) {
        if (visited[i][j] === 0) {
            bfs(i,j);
            cnt1++;
        }
    }
}

// 방문 배열 초기화
for (let i=0; i<n; i++) {
    for (let j=0; j<n; j++) {
        visited[i][j] = 0;
    }
}

// 적록색약인 배열 작업
for (let i=0; i<n; i++) {
    for (let j=0; j<n; j++) {
        if (graph[i][j] === 'G') {
            graph[i][j] = 'R';
        }
    }
}

// 적록색약인 사람
let cnt2 = 0;
for (let i=0; i<n; i++) {
    for (let j=0; j<n; j++) {
        if (visited[i][j] === 0) {
            bfs(i,j);
            cnt2++;
        }
    }
}

console.log(cnt1, cnt2);