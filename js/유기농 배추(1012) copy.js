const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const T = Number(input[0]);
let index = 1;

for (let t=0; t < T; t++) {
    const [m, n, k] = input[index].split(' ').map(Number);
    index++;

    const graph = Array.from({length: n}, () => Array(m).fill(0));

    for (let i=0; i<k; i++) {
        const [a, b] = input[index].split(' ').map(Number);
        graph[b][a] = 1;
        index++;
    }

    const dx = [-1, 1, 0, 0];
    const dy = [0, 0, -1, 1];

    function bfs(x,y) {
        let queue = [];
        queue.push([x,y]);
        // 방문 처리
        graph[x][y] = 2;

        while (queue.length) {
            const [x, y] = queue.shift();
        
            for (let q = 0; q < 4; q++) {
                const nx = x + dx[q];
                const ny = y + dy[q];
        
                if (nx >= 0 && nx < n && ny >= 0 && ny < m && graph[nx][ny] === 1) {
                    graph[nx][ny] = 2;
                    queue.push([nx, ny]);
                }
            }
        }
    }

    let cnt = 0;
    for (let v=0; v < n; v++) {
        for (let c=0; c < m; c++) {
            if (graph[v][c] === 1) {
                bfs(v,c);
                cnt++;
            }
        }
    }
    console.log(cnt);
}