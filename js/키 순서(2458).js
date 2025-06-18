const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const [n, m] = input[0].split(' ').map(Number);
const graph = Array.from({length: n+1}, () => Array(n+1).fill(0));
for (let i=1; i<=m; i++) {
    let [x,y] = input[i].split(' ').map(Number);
    graph[x][y] = 1;
}

// 플로이드 와샬 알고리즘
// i < k, k < j 이면 i < j 
for (let k=1; k<n+1; k++) {
    for (let i=1; i<n+1; i++) {
        for (let j=1; j<n+1; j++) {
            if (graph[i][k] && graph[k][j]) {
                graph[i][j] = 1;
            }
        }
    }
}

let answer = 0;
for (let i=1; i<n+1; i++) {
    let bigger = graph[i].slice(1).reduce((acc, cur) => acc + cur, 0);
    let smaller = 0;
    for (j=1; j<n+1; j++) {
        smaller += graph[j][i];
    }
    if (bigger+smaller === n-1) {
        answer++;
    }
}

console.log(answer);