const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const N = Number(input[0]);
const dp = Array.from({length: N+1}, () => Infinity);
// 배열 생성 방법 2
// const dp = new Array(N+1).fill(Infinity);

dp[0] = 0;
for (let i=3; i<=N; i++) {
    if (i >= 3 && dp[i-3] !== Infinity) {
        dp[i] = Math.min(dp[i], dp[i-3]+1);
    }
    if (i >= 5 && dp[i-5] !== Infinity) {
        dp[i] = Math.min(dp[i], dp[i-5]+1);
    }
}

console.log(dp[N] === Infinity ? -1 : dp[N]);