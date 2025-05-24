const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

let index = 0;
while (true) {
    const [w,h] = input[index].split(' ').map(Number);
    index++;

    if (w === 0 && h === 0) break;

    const graph = input.slice(index, index+h).map((line) => line.split(' ').map(Number));
    const visited = Array.from({length:h}, () => Array(w).fill(false));
    index += h;

    const dx = [-1, 1, 0, 0, -1, -1, 1, 1];
    const dy = [0, 0, -1, 1, -1, 1, -1, 1];

    function bfs(x,y) {
        let queue = [];
        queue.push([x,y]);
        visited[x][y] = true;

        while (queue.length) {
            const [x,y] = queue.shift();

            for (let i=0; i<8; i++) {
                let nx = x + dx[i];
                let ny = y + dy[i];

                if (0 <= nx && nx < h && 0 <= ny && ny < w && !visited[nx][ny] && graph[nx][ny] === 1) {
                    queue.push([nx,ny]);
                    visited[nx][ny] = true;
                }
            }
        }
    }

    let cnt = 0;
    for (let i=0; i<h; i++) {
        for (let j=0; j < w; j++) {
            if (graph[i][j] === 1 && !visited[i][j]) {
                bfs(i,j);
                cnt++;
            }
        }
    }

    console.log(cnt);
}