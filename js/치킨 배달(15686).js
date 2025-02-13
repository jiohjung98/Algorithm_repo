const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const [n, m] = input[0].split(' ').map(Number);
const graph = [];
for (let i=1; i<=n; i++) {
    graph.push(input[i].split(' ').map(Number));
}

const chickenArr = [];
const houseArr = [];

for (let i=0; i<n; i++) {
    for (let j=0; j<n; j++) {
        if (graph[i][j] === 1) {
            houseArr.push([i, j]);
        }
        else if (graph[i][j] === 2) {
            chickenArr.push([i, j]);
        }
    }
}

const arr = [];
let INF = Number.MAX_SAFE_INTEGER;

function backTracking(num, cnt) {
    if (num > chickenArr.length) return;

    if (cnt === m) {
        let resultVal = 0;
        for (let elem of houseArr) {
            let [hx, hy] = elem;
            let MaxVal = Number.MAX_SAFE_INTEGER;

            for (let i=0; i<arr.length; i++) {
                let [cx, cy] = chickenArr[arr[i]];
                MaxVal = Math.min(MaxVal, Math.abs(hx-cx) + Math.abs(hy-cy));
            }
            resultVal += MaxVal
        }
        INF = Math.min(INF, resultVal);
        return;
    }

    arr.push(num);
    backTracking(num+1, cnt+1);
    arr.pop();
    backTracking(num+1, cnt);
    return INF;
}

backTracking(0,0);
console.log(INF);