const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const T = Number(input[0]);
let index = 1;

for (let t=0; t < T; t++) {
    const k = Number(input[index]);
    const n = Number(input[index+1]);
    index += 2;

    const dp = Array.from({length:15}, () => Array(15).fill(0));

    for (let i=1; i<15; i++) {
        dp[0][i] = i;
    }

    for (let i=1; i<15; i++) {
        dp[i][1] = 1;
    }

    for (let x=1; x<15; x++) {
        for (let y=2; y<15; y++) {
            dp[x][y] = dp[x][y-1] + dp[x-1][y]
        }
    }
    console.log(dp[k][n]);
}