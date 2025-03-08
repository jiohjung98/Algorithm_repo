const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const N = Number(input[0]);
const findNum = Number(input[1]);

const graph =  Array.from({length: N}, () => Array(N).fill(0));

// 방향 : 하, 우, 상, 좌
const dx = [1, 0, -1, 0]; 
const dy = [0, 1, 0, -1];

// 첫 위치
let x = 0;
let y = 0;
let num = N**2;
graph[x][y] = num;

let findX = 0;
let findY = 0;

let dir_idx = 0;

while (num > 1) {
    const nx = x + dx[dir_idx];
    const ny = y + dy[dir_idx];

    if (0 <= nx && nx < N && 0 <= ny && ny < N && graph[nx][ny] === 0) {
        num -= 1;
        graph[nx][ny] = num;
        x = nx;
        y = ny;

        if (num === findNum) {
            findX = nx;
            findY = ny;
        }
    } else {
        dir_idx = (dir_idx + 1) % 4;
    }
}

graph.forEach(row => console.log(row.join(' ')));
console.log(findX, findY);