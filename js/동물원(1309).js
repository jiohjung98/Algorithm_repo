const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const N = Number(input[0]);

const dp = Array.from({length: 100001}, () => 0);

dp[1] = 3;
dp[2] = 7;

for (let i=3; i<=N; i++) {
    dp[i] = (dp[i-1] * 2 + dp[i-2]) % 9901;
}

console.log(dp[N]);