const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const [n, m] = input[0].split(' ').map(Number);
const graph = input.slice(1, n+1).map((line) => line.split(' ').map(Number));
const visited = Array.from({length:n}, () => Array(m).fill(false));

const dx = [-1,1,0,0];
const dy = [0,0,-1,1];

let cnt_list = [];

function bfs(x,y) {
    let queue = [];
    queue.push([x,y]);
    visited[x][y] = true;
    let cnt = 1;

    while (queue.length) {
        let [x,y] = queue.shift();

        for (let i=0; i<4; i++) {
            let nx = x + dx[i];
            let ny = y + dy[i];

            if (nx >=0 && nx < n && ny >= 0 && ny < m && !visited[nx][ny] && graph[nx][ny] === 1) {
                queue.push([nx,ny]);
                visited[nx][ny] = true;
                cnt++;
            }
        }
    }
    cnt_list.push(cnt);
}

for (let i=0; i<n; i++) {
    for (let j=0; j<m; j++) {
        if (!visited[i][j] && graph[i][j] === 1) {
            bfs(i,j);
        }
    }
}

if (cnt_list.length > 0) {
    console.log(cnt_list.length);
    console.log(Math.max(...cnt_list));
} else {
    console.log(0);
    console.log(0);
}