const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const [M, N] = input[0].split(' ').map(Number);
const arr = input.slice(1, N+1).map(line => line.split(' ').map(Number));

const dx = [-1,1,0,0];
const dy = [0,0,-1,1];

const queue = [];
let front = 0;

for (let i=0; i < N; i++) {
    for (let j=0; j < M; j++) {
        if (arr[i][j] === 1) {
            queue.push([i,j]);
        }
    }
}

function bfs() {
    while (front < queue.length) {
        // const [x,y] = queue.shift();
        // shift대신 front 포인터 사용하는 이유
        // shift - 배열의 첫 번째 요소를 제거하면서 나머지 요소들을 한 칸씩 당기는 연산 수행
        // -> shift() 시간 복잡도 : O(n) => 큐 크기가 커지면 급격하게 증가 -> 최악의 경우 O(n^2)
        // 대신 front 포인터 사용 - 배열에서 요소 제거하지 않고, 포인터(인덱스)를 하나씩 증가시키면서 다음 요소를 참조 -> O(1)
        // 시간 복잡도 : O(n) 
        const [x, y] = queue[front];
        front++;

        for (let i=0; i < 4; i++) {
            const nx = x + dx[i];
            const ny = y + dy[i];

            if (nx < 0 || nx >= N || ny < 0 || ny >= M) {
                continue;
            }
            if (arr[nx][ny] === 0) {
                arr[nx][ny] = arr[x][y] + 1;
                queue.push([nx,ny]);
            }
        }
    }
}

bfs();
let ans = 0;
for (let a of arr) {
    for (let elem of a) {
        if (elem === 0) {
            console.log(-1);
            return;
        }
        ans = Math.max(ans, elem);
    }
}

console.log(ans-1);
