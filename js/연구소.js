const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const [n, m] = input[0].split(' ').map(Number);
const graph = input.slice(1, n+1).map((line) => line.split(' ').map(Number));

const dx = [-1,1,0,0];
const dy = [0,0,-1,1];
const answerList = [];

function bfs() {
    const queue = [];
    let tmpGraph = graph.map((row) => [...row]);

    for (let i=0; i<n; i++) {
        for (let j=0; j<m; j++) {
            if (tmpGraph[i][j] === 2) {
                queue.push([i,j]);
            }
        }
    }

    while (queue.length > 0) {
        let [x,y] = queue.shift();
        
        for (let i=0; i<4; i++) {
            let nx = x + dx[i];
            let ny = y + dy[i];

            if (nx >= 0 && nx < n && ny >= 0 && ny < m && tmpGraph[nx][ny] === 0) {
                tmpGraph[nx][ny] = 2;
                queue.push([nx,ny]);
            }
        }
    }
    
    const cnt = tmpGraph.flat().filter((v) => v === 0).length;
    answerList.push(cnt);
}

function makeWall(cnt) {
    if (cnt === 3) {
        bfs();
        return;
    }

    for (let i=0; i<n; i++) {
        for (let j=0; j<m; j++) {
            if (graph[i][j] === 0) {
                graph[i][j] = 1;
                makeWall(cnt+1);
                graph[i][j] = 0;
            }
        }
    }
}

makeWall(0);
console.log(Math.max(...answerList));