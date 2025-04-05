let matrix = Array.from({length:100}, () => Array(100).fill(0));
const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

for (let i=0; i<4; i++) {
    let [x1, y1, x2, y2] = input[i].split(' ').map(Number);
    for (let a=y1; a<y2; a++) {
        for (let b=x1; b<x2; b++) {
            matrix[a][b] = 1;
        }
    }
}

let result = 0;

for (let col of matrix) {
    result += col.reduce((acc,cur) => acc+cur, 0);
}

console.log(result);