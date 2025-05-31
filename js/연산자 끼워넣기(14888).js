const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const n = Number(input[0]);
const nums = input[1].split(' ').map(Number);
const operation = input[2].split(' ').map(Number);

let maxValue = -1e9;
let minValue = 1e9;

function bfs(depth, total, plus, minus, multiply, divide) {
    if (depth === n) {
        maxValue = Math.max(maxValue, total);
        minValue = Math.min(minValue, total);
        return;
    }

    if (plus) {
        bfs(depth+1, total+nums[depth], plus-1, minus, multiply, divide);
    }
    if (minus) {
        bfs(depth+1, total-nums[depth], plus, minus-1, multiply, divide);
    }
    if (multiply) {
        bfs(depth+1, total*nums[depth], plus, minus, multiply-1, divide);
    }
    if (divide) {
        bfs(depth+1, parseInt(total/nums[depth]), plus, minus, multiply, divide-1);
    }
}

bfs(1, nums[0], operation[0], operation[1], operation[2], operation[3]);
console.log(maxValue);
console.log(minValue);