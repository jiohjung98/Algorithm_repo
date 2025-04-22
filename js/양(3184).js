const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const [r,c] = input[0].split(' ').map(Number);
// const graph = input.slice(1, r+1).map((line) => line.strip().map(Number));
const graph = input.slice(1, r+1).map((line) => line.trim().split(''))
const visited = Array.from({length:r}, () => Array(c).fill(false));

const dx = [-1,1,0,0];
const dy = [0,0,-1,1];

let total_sheep = [];
let total_wolf = [];

function bfs(x,y) {
    let queue = [];
    queue.push([x,y]);
    visited[x][y] = true;
    let sheep_cnt = 0;
    let wolf_cnt = 0;

    while (queue.length) {
        const [x,y] = queue.shift();

        for (let i=0; i<4; i++) {
            let nx = x + dx[i];
            let ny = y + dy[i];

            if (nx >= 0 && nx < r && ny >= 0 && ny < c && !visited[nx][ny] && graph[nx][ny] !== '#') {
                queue.push([nx,ny]);
                visited[nx][ny] = true;

                if (graph[nx][ny] === 'o') {
                    sheep_cnt++;
                    graph[nx][ny] = 'x';
                }
                else if (graph[nx][ny] === 'v') {
                    wolf_cnt++;
                    graph[nx][ny] = 'x';
                }
            }
        }
    }

    if (sheep_cnt > wolf_cnt) {
        total_sheep.push(sheep_cnt);
    } else {
        total_wolf.push(wolf_cnt);
    }
}

for (let i=0; i<r; i++) {
    for (let j=0; j<c; j++) {
        if (!visited[i][j] && graph[i][j] !== 'o') {
            bfs(i,j);
        }
    }
}

let plus_wolf_cnt = 0;
for (let i=0; i<r; i++) {
    for (let j=0; j<c; j++) {
        if (!visited[i][j] && graph[i][j] === 'v') {
            plus_wolf_cnt++;
        }
    }
}
total_wolf.push(plus_wolf_cnt);

let sheep = total_sheep.reduce((acc,cur) => acc+cur, 0);
let wolf = total_wolf.reduce((acc,cur) => acc+cur, 0);
console.log(sheep, wolf);