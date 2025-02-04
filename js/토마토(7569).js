const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const [M, N, K] = input[0].split(' ').map(Number);

// 3차원 배열 생성
const graph = [];
let index = 1;

for (let k=0; k < K; k++) {
    let layer = [];
    for (let i=0; i < N; i++) {
        layer.push(input[index++].split(' ').map(Number));
    }
    graph.push(layer);
}

const dx = [-1,1,0,0,0,0];
const dy = [0,0,-1,1,0,0];
const dz = [0,0,0,0,1,-1];

const queue = [];
for (let i=0; i<K; i++) {
    for (let j=0; j<N; j++) {
        for (let k=0; k<M; k++) {
            if (graph[i][j][k] === 1) {
                queue.push([i,j,k]);
            } 
        }
    }
}

function bfs() {
    let front = 0;
    while (front < queue.length) {
        // 시간 초과
        // const [z,y,x] = queue.shift();
        const [z,y,x] = queue[front++];

        for (let i=0; i<6; i++) {
            const nx = x + dx[i];
            const ny = y + dy[i];
            const nz = z + dz[i];

            if (nz >= 0 && nz < K && ny >= 0 && ny < N && nx >= 0 && nx < M && graph[nz][ny][nx] === 0) {
                graph[nz][ny][nx]  = graph[z][y][x] + 1;
                queue.push([nz,ny,nx]);
            }
        }
    }
}

let answer = 0;
bfs();

for (g of graph) {
    for (a of g) {
        for (elem of a) {
            if (elem === 0) {
                console.log(-1);
                process.exit(0);
            }
        }
        answer = Math.max(answer, ...a);
    }
}

console.log(answer-1);