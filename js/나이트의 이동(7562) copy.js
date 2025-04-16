const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const T = Number(input[0]);
let index = 1;

const dx = [2, 1, 1, 2, -2, -1, -1, -2];
const dy = [1, 2, -2, -1, -1, -2, 2, 1];

for (let t=0; t<T; t++) {
    const I = Number(input[index]);
    index++;
    const [start_x, start_y] = input[index].split(' ').map(Number);
    index++;
    const [end_x, end_y] = input[index].split(' ').map(Number);
    index++;

    const graph = Array.from({length: I}, () => Array(I).fill(0));
    const visited = Array.from({length: I}, () => Array(I).fill(false));

    function bfs(x,y) {
        let queue = [];
        queue.push([x,y]);
        visited[x][y] = true;

        while (queue.length) {
            const [x,y] = queue.shift();

            if (x === end_x && y === end_y) {
                console.log(graph[x][y]);
                return;
            }

            for (let i=0; i<8; i++) {
                let nx = x + dx[i];
                let ny = y + dy[i];

                if (nx >=0 && nx < I && ny >=0 && ny < I && !visited[nx][ny] && graph[nx][ny] === 0) {
                    visited[nx][ny] = true;
                    graph[nx][ny] = graph[x][y] + 1;
                    queue.push([nx,ny]);
                }
            }
        }
    }

    bfs(start_x, start_y);

}