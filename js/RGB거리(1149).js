const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const N = Number(input[0]);
const dp = Array.from({length: N}, () => Array(3).fill(0));

const rgb_arr = [];
for (let i=0; i<N; i++) {
    const [r, g, b] = input[i+1].split(' ').map(Number);
    rgb_arr.push([r,g,b]);
}

dp[0] = rgb_arr[0];

for (let i=1; i<N; i++) {
    dp[i][0] = Math.min(dp[i-1][1], dp[i-1][2]) + rgb_arr[i][0];
    dp[i][1] = Math.min(dp[i-1][0], dp[i-1][2]) + rgb_arr[i][1];
    dp[i][2] = Math.min(dp[i-1][0], dp[i-1][1]) + rgb_arr[i][2];
}

console.log(Math.min(...dp[N-1]));