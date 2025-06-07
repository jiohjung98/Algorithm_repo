const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const n = Number(input[0]);
const arr = input[1].split(' ').map(Number);
const [b, c] = input[2].split(' ').map(Number);

const new_arr = [];
for (elem of arr) {
    if (elem < b) {
        new_arr.push(0);
    } else {
        new_arr.push(elem-b);
    }
}

let total = 0;

for (elem of new_arr) {
    total += Math.ceil(elem / c);
}

total += new_arr.length;
console.log(total);