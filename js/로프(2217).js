const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const n = Number(input[0]);

const rope = [];
for (let i=1; i<=n; i++) {
    let x = Number(input[i]);
    rope.push(x);
}

const result = [];

rope.sort((a,b) => b-a);

for (let i=0; i<n; i++) {
    result.push(rope[i] * (i+1));
}

console.log(Math.max(...result));