// # 캠퍼스 크기 : N x M
// # 이동 가능 경로 : 상하좌우
// # 도연이가 만날 수 있는 사람의 수를 출력
// # 아무도 만나지못하면 'TT' 출력

// # 입력
// # 첫째 줄 : N, M
// # 둘째 줄 ~ N+1 줄 : 캠퍼스 정보
// # 0 : 빈 공간, X : 벽, I : 도연이, P : 사람
// # I는 한 번만 주어짐 -> I부터 bfs 시작

const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const [N, M] = input[0].split(' ').map(Number);
const campus = input.slice(1, N+1).map((line) => line.trim().split(''))
const visited = Array.from({length:N}, () => Array(M).fill(false));

const dx = [-1,1,0,0];
const dy = [0,0,-1,1];

function bfs(x,y) {
    let queue = [];
    queue.push([x,y]);
    visited[x][y] = true;
    let cnt = 0;

    while (queue.length) {
        const [x,y] = queue.shift();

        for (let i=0; i<4; i++) {
            let nx = x + dx[i];
            let ny = y + dy[i];

            if (nx >= 0 && nx < N && ny >= 0 && ny < M && !visited[nx][ny] && campus[nx][ny] !== 'X') {
                if (campus[nx][ny] === 'P') {
                    cnt++;
                }
                visited[nx][ny] = true;
                queue.push([nx,ny]);
            }
        }
    }
    if (cnt > 0) {
        console.log(cnt);
    } else {
        console.log('TT');
    }
}

for (let i=0; i<N; i++) {
    for (let j=0; j<M; j++) {
        if (campus[i][j] === 'I') {
            bfs(i,j)
        }
    }
}