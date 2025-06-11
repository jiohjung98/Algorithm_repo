const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const [N, L] = input[0].split(' ').map(Number);

const arr = input.slice(1, N+1).map(line => line.split(' ').map(Number));

function checkLine(line, L) {
    let visited = new Array(N).fill(false);
    for (let i=0; i<N-1; i++) {
        if (line[i] === line[i+1]) continue;
        else if (Math.abs(line[i]-line[i+1]) > 1) {
            return false;
        }
        // 왼쪽이 더 클 때
        else if (line[i] > line[i+1]) {
            let temp = line[i+1];
            for (let j=i+1; j<i+L+1; j++) {
                if (j >= 0 && j < N) {
                    if (temp !== line[j]) {
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

        else {
            let temp = line[i];
            for (let j=i-L+1; j<=i; j++) {
                if (j>=0 && j<N) {
                    if (temp !== line[j]) {
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
for (elem of arr) {
    if (checkLine(elem, L)) {
        answer++;
    }
}

// 전치행렬 만들기
function transpose(lines) {
    return lines[0].map((_, cols) => lines.map(line => line[cols]));
}

const arr2 = transpose(arr);
for (elem of arr2) {
    if (checkLine(elem, L)) {
        answer++;
    }
}

console.log(answer);