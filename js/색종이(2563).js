const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const n = Number(input[0]);
const arr = Array.from({length: 100}, () => Array(100).fill(0));

for (let i=1; i<=n; i++) {
    const [y, x] = input[i].split(' ').map(Number);

    for (let j=x; j<x+10; j++) {
        for (let k=y; k<y+10; k++) {
            arr[j][k] = 1;
        }
    }
}

let ans = 0;
for (let x=0; x<100; x++) {
    ans += arr[x].filter(x => 1 === x).length;
}

console.log(ans);