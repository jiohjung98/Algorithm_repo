const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const dx = [-2, -2, 0, 0, 2, 2];
const dy = [-1, 1, -2, 2, -1, 1];

const n = Number(input[0]);
const [r1, c1, r2, c2] = input[1].split(' ').map(Number);

const graph = Array.from({length:n}, () => Array(n).fill(0));

function bfs(x,y) {
    let queue = [];
    queue.push([x,y]);

    while (queue.length) {
        const [x,y] = queue.shift();

        if (x === r2 && y === c2) {
            return graph[x][y];
        }
        
        for (let i=0; i<6; i++) {
            let nx = x + dx[i];
            let ny = y + dy[i];
    
            if (0<=nx && nx<n && 0<=ny && ny<n && graph[nx][ny] ===0 ) {
                queue.push([nx,ny]);
                graph[nx][ny] = graph[x][y] + 1;
            }
        }
    }
    return -1;
}

console.log(bfs(r1,c1));