const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const [n ,m] = input[0].split(' ').map(Number);

const graph = [];
for (let i=1; i<=n; i++) {
    graph.push(input[i].split(' ').map(Number));
}

const dp = Array.from({length: n+1}, () => Array(n+1).fill(0));

for (let i=1; i<=n; i++) {
    for (let j=1; j<=n; j++) {
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + graph[i-1][j-1];
    }
}

for (let i=n+1; i<=n+m; i++) {
    const [x1, y1, x2, y2] = input[i].split(' ').map(Number);

    let answer = dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1];

    console.log(answer);
}