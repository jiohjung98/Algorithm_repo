const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const [M, N] = input[0].split(' ').map(Number);
graph = [];
for (let i=1; i <= M; i++) {
    graph.push(input[i].split(' ').map(Number));
}

const visited = Array.from({length: M}, () => Array(N).fill(false));
const dx = [-1,1,0,0,1,1,-1,-1]
const dy = [0,0,-1,1,1,-1,1,-1]

const bfs = (x,y) => {
    const queue = [];
    queue.push([x,y]);
    visited[x][y] = true;
    let index = 0

    while (index < queue.length) {
        const [x,y] = queue[index++];

        for (let i=0; i<8; i++) {
            const nx = x + dx[i];
            const ny = y + dy[i];

            if (nx >=0 && nx < M && ny >=0 && ny < N && !visited[nx][ny] && graph[nx][ny] === 1) {
                visited[nx][ny] = true;
                queue.push([nx,ny]);
            }
        }
    }
}

let cnt = 0;
for (let i=0; i<M; i++) {
    for (let j=0; j<N; j++) {
        if (graph[i][j] === 1 && !visited[i][j]) {
            bfs(i,j);
            cnt++;
        }
    }
}

console.log(cnt);