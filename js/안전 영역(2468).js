const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const N = Number(input[0]);
// slice(1) - 첫 번째 줄을 제외한 나머지 줄 가져옴
const arr = input.slice(1).map(line => line.split(' ').map(Number));

// flat - 2차원 배열을 1차원 배열로 변환
const maxValue = Math.max(...arr.flat());

const answerArr = [];

for (let i=1; i < maxValue; i++) {
    // 얕은 복사 방법
    // const rainArr = [...arr];
    // 깊은 복사 방법
    // const rainArr = structuredClone(arr); -> 최신 브라우저에서만 지원
    const rainArr = arr.map(row => [...row]);
    for (let j=0; j < N; j++) {
        for (let k=0; k < N; k++) {
            if (arr[j][k] <= i) {
                rainArr[j][k] = 0;
            } else {
                rainArr[j][k] = 1;
            }
        }
    }

    const dx = [-1,1,0,0];
    const dy = [0,0,-1,1];

    function bfs(x,y) {
        const queue = [];
        queue.push([x,y]);
        // 방문 처리
        rainArr[x][y] = 2;

        while (queue.length) {
            const [x,y] = queue.shift();

            for (let t=0; t < 4; t++) {
                const nx = x + dx[t];
                const ny = y + dy[t];

                if (nx < 0 || nx >= N || ny < 0 || ny >= N) {
                    continue;
                }
                if (rainArr[nx][ny] === 0) {
                    continue;
                }
                if (rainArr[nx][ny] === 1) {
                    rainArr[nx][ny] = 2;
                    queue.push([nx,ny]);
                }
            }
        }
    }
    let cnt = 0;
    for (let a=0; a < N; a++) {
        for (let b=0; b < N; b++) {
            if (rainArr[a][b] == 1) {
                bfs(a,b);
                cnt++;
            }
        }
    }
    answerArr.push(cnt);
}

// Math.max(answerArr) -> NaN 반환 : 배열 자체를 넘기기 때문
// 따라서 전개연산자를 사용해서 배열 요소를 개별 인자로 펼침
// ex) answerArr = [1,2,3,4,5]
// Math.max(...answerArr) = Math.max(1,2,3,4,5)
console.log(answerArr.length === 0 ? 1 : Math.max(...answerArr));