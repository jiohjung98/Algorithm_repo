const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const T = Number(input[0]);

for (let i=1; i< T+1; i++) {
    const N = Number(input[i]);
    const dp = Array(N+1).fill(0);

    for (let j=1; j<=N; j++) {
        if (j === 1) dp[j] = 1;
        else if (j === 2) dp[j] = 2;
        else if (j === 3) dp[j] = 4;
        else dp[j] = dp[j-1] + dp[j-2] + dp[j-3];
    }

    console.log(dp[N]);
}