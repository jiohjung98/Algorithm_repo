const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const n = Number(input[0]);
const graph = input.slice(1).map((line) => line.split(' ').map(Number));

let maxRain = 0;
for (let i=0 ; i<n; i++) {
    maxRain = Math.max(maxRain, Math.max(...graph[i]));
}

const visited = Array.from({length:n}, () => Array(n).fill(false));

const dx = [-1, 1, 0, 0];
const dy = [0, 0, -1, 1];

let cntArr = [];

for (let i=0; i<maxRain; i++) {
    // 원본 영역과 방문 배열 깊은 복사해서 사용
    const rainArr = graph.map(row => [...row]);
    const rainVisited = visited.map(row => [...row]);

    for (let j=0; j<n; j++) {
        for (let k=0; k<n; k++) {
            // 최대 빗물보다 영역높이가 작으면
            if (graph[j][k] <= i) {
                rainArr[j][k] = 0;
            } else {
                rainArr[j][k] = 1;
            }
        }
    }

    function bfs(x,y) {
        let queue = [];
        queue.push([x,y]);
        rainVisited[x][y] = true;
        let front = 0;

        while (front < queue.length) {
            const [x,y] = queue[front];
            front++;

            for (let a=0; a<4; a++) {
                let nx = x + dx[a];
                let ny = y + dy[a];

                if (nx >=0 && nx <n && ny >=0 && ny < n && !rainVisited[nx][ny] && rainArr[nx][ny] === 1) {
                    queue.push([nx,ny]);
                    rainVisited[nx][ny] = true;
                }
            }
        }
    }

    let cnt = 0;
    for (let w=0; w<n; w++) {
        for (let m=0; m<n; m++) {
            if (!rainVisited[w][m] && rainArr[w][m] === 1) {
                bfs(w,m);
                cnt++;
            } 
        }
    }
    cntArr.push(cnt);
}

const maxSafe = Math.max(...cntArr);
console.log(maxSafe === 0 ? 1 : maxSafe);