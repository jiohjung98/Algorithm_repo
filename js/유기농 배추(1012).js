const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const T = Number(input[0]);
let index = 1;

for (let t=0; t < T; t++) {
    const [M, N, K] = input[index].split(' ').map(Number);
    index++;

    const graph = Array.from({length: N}, () => Array(M).fill(0));

    for (let j=0; j < K; j++) {
        const [a, b] = input[index].split(' ').map(Number);
        graph[b][a] = 1
        index++;
    }

    const dx = [-1, 1, 0, 0];
    const dy = [0, 0, -1, 1];

    function bfs(x,y) {
        let queue = [];
        queue.push([x,y]);
        graph[x][y] = 0;

        while (queue.length) {
            const [x, y] = queue.shift();

            for (let a=0; a < 4; a++) {
                const nx = x + dx[a];
                const ny = y + dy[a];

                if (nx < 0 || nx >= N || ny < 0 || ny >= M) {
                    continue;
                }
                if (graph[nx][ny] === 0) {
                    continue;
                }
                if (graph[nx][ny] === 1) {
                    graph[nx][ny] = 0;
                    queue.push([nx, ny]);
                }
            }
        }
    }

    let cnt = 0;
    for (let n=0; n < N; n++) {
        for (let m=0; m < M; m++) {
            if (graph[n][m] === 1) {
                bfs(n,m);
                cnt++;
            }
        }
    }
    console.log(cnt);
}