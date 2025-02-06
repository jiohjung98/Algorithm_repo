const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const n = Number(input[0]);

if (n==1) {
    console.log(1 % 10007);
    process.exit();
}

dp = Array.from({length:n+1}, () => 0);

dp[1] = 1;
dp[2] = 2;
for (let i=3; i<=n; i++) {
    dp[i] = (dp[i-1] + dp[i-2]) % 10007;
}

console.log(dp[n]);