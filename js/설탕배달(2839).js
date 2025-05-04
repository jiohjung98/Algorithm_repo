const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const sugar = Number(input[0]);
const dp = Array.from({length: sugar+1}, () => Infinity);
dp[0] = 0;

for (let i=3; i<sugar+1; i++) {
    if (dp[i-3] !== Infinity) {
        dp[i] = Math.min(dp[i], dp[i-3]+1);
    }
    if (i >= 5 && dp[i-5] !== Infinity) {
        dp[i] = Math.min(dp[i], dp[i-5]+1);
    }
}

console.log(dp[sugar] !== Infinity ? dp[sugar] : -1);