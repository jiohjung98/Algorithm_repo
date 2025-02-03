// const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

// const n = Number(input[0]);
// const arr = input.slice(1).map(line => line.split(''));
// const visited = Array.from({length: n}, () => Array(n).fill(false));

// const dx = [-1,1,0,0];
// const dy = [0,0,-1,1];

// function bfs(x,y) {
//     const queue = [];
//     queue.push([x,y]);
//     visited[x][y] = true;

//     while (queue.length) {
//         const [x,y] = queue.shift();

//         for (let i=0; i<4; i++) {
//             const nx = x + dx[i];
//             const ny = y + dy[i];

//             if (nx >= 0 && nx < n && ny >=0 && ny < n && !visited[nx][ny]) {
//                 if (arr[x][y] === arr[nx][ny]) {
//                     visited[nx][ny] = true;
//                     queue.push([nx,ny]);
//                 }
//             }
//         }
//     }
// }

// let cnt1 = 0;
// for (let i=0; i<n; i++) {
//     for (let j=0; j<n; j++) {
//         if (!visited[i][j]) {
//             bfs(i,j);
//             cnt1++;
//         }
//     }
// }

// // 방문 배열 초기화
// for (let i=0; i<n; i++) {
//     for (let j=0; j<n; j++) {
//         visited[i][j] = false;
//     }
// }

// // 원본 배열 적록색약 사람 시점 변경
// for (let i=0; i<n; i++) {
//     for (let j=0; j<n; j++) {
//         if (arr[i][j] === 'G') {
//             arr[i][j] = 'R';
//         }
//     }
// }

// let cnt2 = 0;
// for (let i=0; i<n; i++) {
//     for (let j=0; j<n; j++) {
//         if (!visited[i][j]) {
//             bfs(i,j);
//             cnt2++;
//         }
//     }
// }

// console.log(cnt1, cnt2);


// 개선 코드
const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const n = Number(input[0]);
const arr = input.slice(1).map(line => line.split(''));

const dx = [-1, 1, 0, 0];
const dy = [0, 0, -1, 1];

function bfs(x, y, visited, isBlind) {
    const queue = [[x, y]];
    visited[x][y] = true;
    const color = arr[x][y];

    while (queue.length) {
        const [cx, cy] = queue.shift();

        for (let i = 0; i < 4; i++) {
            const nx = cx + dx[i];
            const ny = cy + dy[i];

            if (nx >= 0 && nx < n && ny >= 0 && ny < n && !visited[nx][ny]) {
                // 적록색약 시점에서는 'R'과 'G'를 같은 색으로 취급
                if (isBlind) {
                    if ((color === 'R' || color === 'G') && (arr[nx][ny] === 'R' || arr[nx][ny] === 'G')) {
                        visited[nx][ny] = true;
                        queue.push([nx, ny]);
                    }
                } else {
                    // 일반 시점에서는 같은 색일 경우에만 이동
                    if (arr[nx][ny] === color) {
                        visited[nx][ny] = true;
                        queue.push([nx, ny]);
                    }
                }
            }
        }
    }
}

// 두 개의 방문 배열을 따로 사용 (초기화 작업 최소화)
const visited1 = Array.from({ length: n }, () => Array(n).fill(false));
const visited2 = Array.from({ length: n }, () => Array(n).fill(false));

let cnt1 = 0, cnt2 = 0;

// 일반인 영역 탐색
for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
        if (!visited1[i][j]) {
            bfs(i, j, visited1, false);
            cnt1++;
        }
    }
}

// 적록색약 시점 탐색
for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
        if (!visited2[i][j]) {
            bfs(i, j, visited2, true);
            cnt2++;
        }
    }
}

console.log(cnt1, cnt2);