const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const [n, m] = input[0].split(' ').map(Number);
const graph = input.slice(1).map((line) => line.split(' ').map(Number));

const dx = [-1, 1, 0, 0];
const dy = [0, 0, -1, 1];

let answerList  = [];

function Bfs() {
    let queue = [];
    // js 깊은 복사
    let tmpGraph = graph.map((v) => [...v]);
    for (let i=0; i<n; i++) {
        for (let j=0; j<m; j++) {
            if (tmpGraph[i][j] === 2) {
                queue.push([i,j]);
            }
        }
    }
    let front = 0;

    while (front < queue.length) {
        const [x,y]= queue[front];
        front++;

        for (let a=0; a<4; a++) {
            let nx = x + dx[a];
            let ny = y + dy[a];

            if (nx >=0 && nx < n && ny >= 0 && ny < m && tmpGraph[nx][ny] === 0) {
                tmpGraph[nx][ny] = 2;
                queue.push([nx,ny]);
            }
        }
    }
    
    // js 2차원 배열에서 특정값 카운트 - flat, filter 사용
    const cnt = tmpGraph.flat().filter((v) => v === 0).length;
    answerList.push(cnt);
}

function MakeWall(cnt) {
    if (cnt === 3) {
        Bfs();
        return;
    }

    for (let i=0; i<n; i++) {
        for (let j=0; j<m; j++) {
            if (graph[i][j] === 0) {
                graph[i][j] = 1;
                MakeWall(cnt+1);
                graph[i][j] = 0;
            }
        }
    }
}

MakeWall(0);
console.log(Math.max(...answerList));