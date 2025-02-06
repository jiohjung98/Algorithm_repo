const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const n = Number(input[0]);
arr = [];
for (let i=1; i<=n; i++) {
    const a = input[i].split(' ').map(Number);
    arr.push(a);
}

const dp = Array.from({length: n+1}, () => 0);
for (let i=0; i<n; i++) {
    for (let j=i+arr[i][0]; j<=n; j++) {
        if (dp[j] < dp[i] + arr[i][1]) {
            dp[j] = dp[i] + arr[i][1];
        }
    }
}

console.log(Math.max(...dp));