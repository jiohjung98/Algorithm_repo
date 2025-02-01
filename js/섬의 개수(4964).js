const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

let index = 0;

while (true) {
    const [w, h] = input[index].split(' ').map(Number);
    index++;

    if (w === 0 && h === 0) break;
    const graph = [];
    for (let i=0; i<h; i++) {
        graph.push(input[index].split(' ').map(Number));
        index++;
    }

    const dx = [-1,1,0,0,-1,-1,1,1];
    const dy = [0,0,-1,1,1,-1,1,-1];

    function bfs(x,y) {
        const queue = [];
        queue.push([x,y]);
        graph[x][y] = 2;

        while (queue.length) {
            const [x,y] = queue.shift();

            for (let i=0; i<8; i++) {
                const nx = x + dx[i];
                const ny = y + dy[i];

                if (nx < 0 || nx >= h || ny < 0 || ny >= w) continue;
                if (graph[nx][ny] === 0) continue;
                if (graph[nx][ny] === 1) {
                    graph[nx][ny] = 2;
                    queue.push([nx,ny]);
                }
            }
        }
    }

    let cnt = 0;
    for (let i=0; i<h; i++) {
        for (let j=0; j<w; j++) {
            if (graph[i][j] === 1) {
                bfs(i,j);
                cnt++;
            }
        }
    }

    console.log(cnt);
}