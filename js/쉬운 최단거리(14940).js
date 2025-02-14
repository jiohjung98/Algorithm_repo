const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const [n, m] = input[0].split(' ').map(Number);
const arr = [];
for (let i=1; i<=n; i++) {
    arr.push(input[i].split(' ').map(Number));
}

const arrCopy = JSON.parse(JSON.stringify(arr));
const visited = Array.from({length: n}, () => Array(m).fill(0));

const dx = [-1,1,0,0];
const dy = [0,0,-1,1];

function bfs(x,y) {
    const queue = [];
    queue.push([x,y]);
    visited[x][y] = 1;
    arr[x][y] = 0;

    // let index = 0;
    while (queue.length) {
        const [x,y] = queue.shift();

        for (let i=0; i<4; i++) {
            const nx = x + dx[i];
            const ny = y + dy[i];

            if (nx >=0 && nx < n && ny >=0 && ny < m && arr[nx][ny] !== 0 && !visited[nx][ny]) {
                arr[nx][ny] = arr[x][y] + 1;
                visited[nx][ny] = 1;
                queue.push([nx,ny]);
            }
        }
    }
}

let arriveX = 0;
let arriveY = 0;


for (let i=0; i<n; i++) {
    for (let j=0; j<m; j++) {
        if (arr[i][j] === 2) {
            arriveX = i;
            arriveY = j;
            break;
        }
    }
}

bfs(arriveX, arriveY);

for (let i=0; i<n; i++) {
    for (let j=0; j<m; j++) {
        if (!visited[i][j]) {
            if (arrCopy[i][j] === 1) {
                arr[i][j] = -1;
            }
            else {
                arr[i][j] = 0;
            }
        }
    }
}

for (let elem of arr) {
    console.log(elem.join(' '));
}