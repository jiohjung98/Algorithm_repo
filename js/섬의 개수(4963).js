const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

let index = 0;

while (true) {
    const [w, h] = input[index].split(' ').map(Number);
    index++;
    // 입력이 0, 0이면 종료
    if (w === 0 && h === 0) break;

    const graph = input.slice(index, index+h).map((line) => line.split(' ').map(Number));
    const visited = Array.from({length: h}, () => Array(w).fill(0));
    index += h;

    // 가로, 세로, 대각선 범위 설정
    const dx = [-1, 1, 0, 0, -1, -1, 1, 1];
    const dy = [0, 0, -1, 1, -1, 1, -1, 1];

    function bfs(x,y) {
        let queue = [];
        queue.push([x,y]);
        visited[x][y] = 1;

        while (queue.length) {
            const [x,y] = queue.shift();

            for (let i=0; i<8; i++) {
                let nx = x + dx[i];
                let ny = y + dy[i];

                if (nx >=0 && nx < h && ny >=0 && ny < w && visited[nx][ny] === 0 && graph[nx][ny] === 1) {
                    visited[nx][ny] = 1;
                    queue.push([nx,ny]);
                }
            }
        }
    }
    let cnt = 0;
    for (let x=0; x<h; x++) {
        for (let y=0; y<w; y++) {
            if (graph[x][y] === 1 && visited[x][y] === 0) {
                bfs(x,y);
                cnt++;
            }
        }
    }

    console.log(cnt);
}