const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const T = Number(input[0]);  
let index = 1; 

for (let t = 0; t < T; t++) {
    const n = Number(input[index]);  
    const arr = [
        input[index + 1].split(' ').map(Number),
        input[index + 2].split(' ').map(Number)  
    ];
    
    index += 3;

    if (n === 1) {
        console.log(Math.max(arr[0][0], arr[1][0]));
        continue;
    }

    const dp = Array.from({ length: 2 }, () => Array(n).fill(0));

    dp[0][0] = arr[0][0];
    dp[1][0] = arr[1][0];

    dp[0][1] = arr[1][0] + arr[0][1];
    dp[1][1] = arr[0][0] + arr[1][1];

    if (n === 2) {
        console.log(Math.max(dp[0][1], dp[1][1]));
        continue;
    }

    for (let i = 2; i < n; i++) {
        dp[0][i] = Math.max(dp[1][i - 1], dp[1][i - 2]) + arr[0][i];
        dp[1][i] = Math.max(dp[0][i - 1], dp[0][i - 2]) + arr[1][i];
    }

    console.log(Math.max(dp[0][n - 1], dp[1][n - 1]));
}