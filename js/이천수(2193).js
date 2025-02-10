const fs = require('fs');
const n = Number(fs.readFileSync('/dev/stdin').toString().trim());

const dp = Array(n + 1).fill(0);
dp[1] = 1;

for (let i = 2; i <= n; i++) {
    dp[i] = dp[i - 2] + dp[i - 1];
}

console.log(dp[n]);