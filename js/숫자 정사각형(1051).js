const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const [n, m] = input[0].split(' ').map(Number);
const arr = [];
for (let i=1; i<=n; i++) {
    arr.push(input[i].split('').map(Number));
}