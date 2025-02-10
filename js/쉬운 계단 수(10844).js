const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const n = Number(input[0]);

const dp = Array.from({ length: n+1 }, () => Array(10).fill(0));

for (let i=1; i<=9; i++) {
    dp[1][i] = 1;
}

for (let i=2; i<=n; i++) {
    for (let j=0; j<10; j++) {
        if (j === 0) {
            dp[i][j] = dp[i-1][1] % 1000000000;
        }
        else if (j === 9) {
            dp[i][j] = dp[i-1][8] % 1000000000;
        }
        else {
            dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1]) % 1000000000;
        }
    }
}

console.log(dp[n].reduce((acc, num) => (acc + num) % 1000000000, 0));