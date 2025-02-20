const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const [n, m] = input[0].split(' ').map(Number);
const arr = Array.from({length:n+1}, () => []);

for (let i=1; i<=m; i++) {
    let [x, y] = input[i].split(' ').map(Number);
    arr[x].push(y);
    arr[y].push(x);
}

function bfs(start) {
    const queue = [];
    queue.push([start]);
    const visited = Array(n+1).fill(0);

    while (queue.length) {
        const now = queue.shift();
        for (let next of arr[now]) {
            // 방문 전이라면
            if (visited[next] === 0) {
                visited[next] = visited[now] + 1;
                queue.push([next]);
            }
        }
    }

    return [...visited].reduce((acc,cur) => acc+cur, 0);
}

let minValue = Infinity;
let answer = 0;

for (let i=1; i<=n; i++) {
    let totalDistance = bfs(i);
    if (totalDistance < minValue) {
        minValue = totalDistance
        answer = i;
    }
}

console.log(answer);