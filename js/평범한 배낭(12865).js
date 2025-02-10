const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const [n, k] = input[0].split(' ').map(Number);
const bag = [[0,0]];

for (let i=1; i<=n; i++) {
    const [w, v] = input[i].split(' ').map(Number);
    bag.push([w,v]);
}

const dp = Array.from({length: n+1}, () => Array(k+1).fill(0));

for (let i=1; i<=n; i++) {
    const [w, v] = bag[i];
    for (let j=1; j<=k; j++) {
        if (j < w) {
            dp[i][j] = dp[i-1][j];
        } else {
            dp[i][j] = Math.max(dp[i-1][j-w] + v, dp[i-1][j]);
        }
    }
}

console.log(dp[n][k]);