const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const [N, L] = input[0].split(' ').map(Number);

const arr = input.slice(1, N+1).map((line) => line.split(' ').map(Number));

function checkLines(lines, L) {
    let visited = new Array(N).fill(false);
    for (let i=0; i< N-1; i++) {
        // 같으면
        if (lines[i] === lines[i+1]) {
            continue;
        }
        // 차이가 1 이상이면
        else if (Math.abs(lines[i] - lines[i+1]) > 1) {
            return false;
        }
        // 왼쪽이 더 크면
        else if (lines[i] > lines[i+1]) {
            let temp = lines[i+1];
            for (let j=i+1; j<i+L+1; j++) {
                // 범위 내에 들어오면
                if (j >= 0 && j < N) {
                    // L 길이만큼 돌면서 높이가 동일하지 않으면
                    if (temp !== lines[j]) {
                        return false;
                    }
                    // 방문한 곳이면
                    else if (visited[j]) {
                        return false;
                    }
                    visited[j] = true;
                }
                else {
                    return false;
                }
            }
        }
        // 오른쪽이 더 크면
        else {
            let temp = lines[i];
            for (let j=i-L+1; j <=i; j++) {
                // 범위 내에 들어오면
                if (j >= 0 && j < N) {
                    if (temp != lines[j]) {
                        return false;
                    }
                    else if (visited[j]) {
                        return false;
                    }
                    visited[j] = true;
                }
                else {
                    return false;
                }
            }
        }
    }
    return true;
}

let answer = 0;
for (let elem of arr) {
    if (checkLines(elem, L)) {
        answer++;
    }
}

const transformColsAndRows = (lines) => {
    return lines[0].map((_, cols) => lines.map(line => line[cols]));
}

const arr2 = transformColsAndRows(arr);
for (let elem of arr2) {
    if (checkLines(elem, L)) {
        answer++;
    }
}

console.log(answer);