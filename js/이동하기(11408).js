const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const [n, m] = input[0].split(' ').map(Number);

const miro = [];
for (let i=1; i<=n; i++) {
    miro.push(input[i].split(' ').map(Number));
}

// 전치 행렬
const miro_reverse = Array.from({length:m}, () => Array(n).fill(0));
for (let i=0; i<n; i++) {
    for (let j=0; j<m; j++) {
        miro_reverse[j][i] = miro[i][j];
    }
}

const dp = Array.from({ length: n }, () => Array(m).fill(0));
dp[0][0] = miro[0][0];

for (let i = 1; i < m; i++) {
    dp[0][i] = dp[0][i-1] + miro[0][i];
}

for (let j = 1; j < n; j++) {
    dp[j][0] = dp[j-1][0] + miro_reverse[0][j];
}

for (let i = 1; i < n; i++) {
    for (let j = 1; j < m; j++) {
        dp[i][j] = Math.max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + miro[i][j];
    }
}

console.log(dp[n-1][m-1]);