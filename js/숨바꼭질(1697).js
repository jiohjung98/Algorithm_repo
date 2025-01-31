const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const [N, K] = input.split(' ').map(Number);
const visited = Array.from({length: 100001}, () => false);

function bfs(start) {
    const queue = [];
    queue.push([start, 0])

    while (queue.length) {
        const [cur, time] = queue.shift();

        if (cur === K) {
            return time;
        }

        for (let i of [cur-1, cur+1, cur*2]) {
            if (i >= 0 && i <= 100000 && !visited[i]) {
                visited[i] = true;
                queue.push([i, time+1]);
            }
        }
    }
}