const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const n = Number(input[0]);

const dp = Array.from({length: n+1}, () => 0);

for (let i=2; i<n+1; i++) {
    dp[i] = dp[i-1] + 1;
    if (i % 2 === 0) {
        dp[i] = Math.min(dp[i], Math.floor(dp[i/2])+1);
    }
    if (i % 3 === 0) {
        dp[i] = Math.min(dp[i], Math.floor(dp[i/3])+1);
    }
}

console.log(dp[n]);