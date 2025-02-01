const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const T = Number(input[0]);
let index = 1;

for (let t=0; t < T; t++) {
    const L = Number(input[index]);
    index++;

    const [start_x, start_y] = input[index].split(' ').map(Number);
    index++;

    const [end_x, end_y] = input[index].split(' ').map(Number);
    index++;

    const arr = Array.from({length: L}, () => Array(L).fill(0));

    const dx = [-1, -2, -2, -1, 1, 2, 2, 1];
    const dy = [-2, -1, 1, 2, 2, 1, -1, -2];

    function bfs(x,y) {
        const queue = [];
        queue.push([x,y]);
        arr[x][y] = 1;

        while (queue.length) {
            const [x,y] = queue.shift();

            if (x === end_x && y === end_y) {
                console.log(arr[x][y]-1);
                return;
            }

            for (let i=0; i<8; i++) {
                const nx = x + dx[i];
                const ny = y + dy[i];

                if (nx < 0 || nx >= L || ny < 0 || ny >= L) continue;

                if (arr[nx][ny] === 0) {
                    arr[nx][ny] = arr[x][y] + 1;
                    queue.push([nx,ny]);
                }
            }
        }
    }
    bfs(start_x, start_y);
}