const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

function checkNums(front, back, oper) {
    if (oper === '<') {
        if (front > back) {
            return false;
        }
    }
    else if (oper === '>') {
        if (front < back) {
            return false;
        }
    }
    return true;
}

function dfs(cnt, nums) {
    if (cnt === k+1) {
        answer_list.push(nums);
        return;
    }
    for (let i=0; i<=9; i++) {
        if (visited[i]) continue;
        else {
            if (cnt === 0 || checkNums(Number(nums[nums.length-1]), i, operation[cnt-1])) {
                visited[i] = true;
                dfs(cnt+1, nums + i.toString())
                visited[i] = false;
            }
        }
    }
}

const k = Number(input[0]);
const operation = input[1].split(' ').map(String);

let visited = new Array(10).fill(false);
let answer_list = [];

dfs(0, '');
answer_list.sort((a,b) => a-b);
console.log(answer_list[answer_list.length-1]);
console.log(answer_list[0]);