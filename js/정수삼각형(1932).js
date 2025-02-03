const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const n = Number(input[0]);
const dp = input.slice(1).map(line => line.split(' ').map(Number));

var k = 2;
for (let i=1; i<n; i++) {
    for (let j=0; j<k; j++) {
        if (j === 0) {
            dp[i][j] = dp[i][j] + dp[i-1][j];
        }
        else if (j === i) {
            dp[i][j] = dp[i][j] + dp[i-1][j-1];
        }
        else {
            dp[i][j] = Math.max(dp[i-1][j-1], dp[i-1][j]) + dp[i][j];
        }
    }
    k++;
}

console.log(Math.max(...dp[n-1]));