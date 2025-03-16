const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const n = input[0];

const comp = n.length - 1;
let ans = 0;

for (let i=0; i <comp; i++) {
    ans += 9 *(10**i) *(i+1);
}

ans += (parseInt(n) - (10**comp) + 1) * (comp + 1);

console.log(ans);