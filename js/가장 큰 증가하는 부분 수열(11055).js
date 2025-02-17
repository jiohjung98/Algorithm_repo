const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const n = Number(input[0]);
const arr = input[1].split(' ').map(Number);

const dp = Array.from({length: n}, () => 0);
dp[0] = arr[0];

for (let i=1; i<n; i++) {
    for (let j=0; j<i; j++) {
        if (arr[i] > arr[j]) {
            dp[i] = Math.max(dp[i], arr[i] + dp[j]);
        } else {
            dp[i] = Math.max(dp[i], arr[i])
        }
    }
}

console.log(Math.max(...dp));