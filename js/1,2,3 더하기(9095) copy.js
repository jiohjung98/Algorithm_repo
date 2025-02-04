const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const N = Number(input[0]);
const stairs = [0];
for (let n=1; n <= N; n++) {
    a = Number(input[n]);
    stairs.push(a);
}

if (N === 1) console.log(stairs[1]);
else if (N === 2) console.log(stairs[1] + stairs[2]);
else {
    const dp = Array.from({length: N+1}, () => 0);
    dp[1] = stairs[1];
    dp[2] = dp[1] + stairs[2];
    for (let i=3; i<=N; i++) {
        dp[i] = Math.max(dp[i-2], dp[i-3] + stairs[i-1]) + stairs[i];
    }
    console.log(dp[N]);
}