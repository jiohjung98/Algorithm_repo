const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const n = Number(input[0]);
const p = Array(10001).fill(0);
const dp = Array(10001).fill(0);

for (let i=1; i<=n; i++) {
    p[i] = Number(input[i]);
}

dp[1] = p[1];
dp[2] = p[1] + p[2];

for (let i=3; i<=n; i++) {
    dp[i] = Math.max(p[i]+p[i-1]+dp[i-3], p[i]+dp[i-2], dp[i-1]);
}

console.log(Math.max(...dp));