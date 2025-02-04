const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const [N, M, V] = input[0].split(' ').map(Number);
const graph = Array.from({length: N+1}, () => Array(N+1).fill(0));

for (let i=1; i <= M; i++) {
    const [a, b] = input[i].split(' ').map(Number);
    graph[a][b] = 1;
    graph[b][a] = 1;
}

const dfs_visited_arr = new Array(N+1).fill(0);
const bfs_visited_arr = new Array(N+1).fill(0);

function dfs(x) {
    dfs_visited_arr[x] = 1;
    process.stdout.write(x + ' ');
    for (let i=1; i <= N; i++) {
        if (graph[x][i] === 1 && dfs_visited_arr[i] === 0) {
            dfs(i);
        }
    }
}

function bfs(x) {
    const queue = [x];
    bfs_visited_arr[x] = 1;

    while (queue.length) {
        const y = queue.shift();
        process.stdout.write(y + ' ');

        for (let i=1; i <= N; i++) {
            if (graph[y][i] ===1 && bfs_visited_arr[i] === 0) {
                bfs_visited_arr[i] = 1;
                queue.push(i);
            }
        }
    }
}

dfs(V);
console.log();
bfs(V);
console.log();