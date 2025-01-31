const input = require('fs').readFileSync('/dev/stdin').toString().split('\n');

const N = +input.shift();
const arr = input.slice(1, N+1).map((line) => line.split("").map(Number));