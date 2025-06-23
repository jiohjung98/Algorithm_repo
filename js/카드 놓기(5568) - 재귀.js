const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const n = Number(input[0]);
const k = Number(input[1]);
const arr = input.slice(2, 2+n).map(Number);

let visited = Array.from({length: n}, () => false);

let card_list = [];
let result = [];

const backtracking = () => {
    if (card_list.length === k) {
        if (!result.includes(card_list.join(''))) {
            result.push(card_list.join(''));
        }
        return;
    }
    for (let i=0; i<arr.length; i++) {
        if (!visited[i]) {
            visited[i] = true;
            card_list.push(arr[i]);
            backtracking();
            visited[i] = false;
            card_list.pop();
        }
    }
}

backtracking();
console.log(result.length);