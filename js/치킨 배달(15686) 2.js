const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const [n, m] = input[0].split(' ').map(Number);
const arr = [];
const home_list = [];
const chicken_list = [];

for (let i=1; i<=n; i++) {
    arr.push(input[i].split(' ').map(Number));
    for (let j=0; j<n; j++) {
        if (arr[i-1][j] === 1) {
            home_list.push([i,j]);
        } else if (arr[i-1][j] === 2) {
            chicken_list.push([i,j]);
        }
    }
}

let visited = new Array(chicken_list.length).fill(false);
let cnt_list = [];

function backtracking(idx, cnt) {
    if (cnt === m) {
        let total = 0;
        for (let [hx, hy] of home_list) {
            let min_dist = Infinity;
            for (let i=0; i<chicken_list.length; i++) {
                if (visited[i]) {
                    let [cx, cy] = chicken_list[i];
                    let dist = Math.abs(cx-hx) + Math.abs(cy-hy);
                    min_dist = Math.min(min_dist, dist);
                }
            }
            total += min_dist;
        }
        cnt_list.push(total);
        return;
    }

    for (let i=idx; i<chicken_list.length; i++) {
        if (!visited[i]) {
            visited[i] = true;
            backtracking(i+1, cnt+1);
            visited[i] = false;
        }
    }
}

backtracking(0,0);
console.log(Math.min(...cnt_list));