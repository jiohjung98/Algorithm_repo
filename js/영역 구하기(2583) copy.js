const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const [m, n, k] = input[0].split(' ').map(Number);
const graph = Array.from({length: m}, () => Array(n).fill(0));
const visited = Array.from({length: m}, () => Array(n).fill(false));

const dx = [-1, 1, 0, 0];
const dy = [0, 0, -1, 1];

for (let i=1; i<k+1; i++) {
    const [bottom_x, bottom_y, top_x, top_y] = input[i].split(' ').map(Number);
    for (let x=bottom_y; x<top_y; x++) {
        for (let y=bottom_x; y<top_x; y++) {
            graph[x][y] = 1;
        }
    }
}

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

            if (nx >=0 && nx < m && ny >=0 && ny < n && !visited[nx][ny] && graph[nx][ny] === 0) {
                visited[nx][ny] = true;
                queue.push([nx,ny]);
                cnt++;
            }
        }
    }

    cnt_list.push(cnt);
}

for (let i=0; i<m; i++) {
    for (let j=0; j<n; j++) {
        if (!visited[i][j] && graph[i][j] === 0) {
            bfs(i,j);
        }
    }
}

cnt_list.sort((a,b) => a-b);
console.log(cnt_list.length);
console.log(cnt_list.join(' '));