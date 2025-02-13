const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const n = input[0].split('');

const card = Array.from({length: 10}, () => 0);

for (let elem of n) {
    if (elem === '6') {
        card[9] += 1;
    }
    else {
        card[Number(elem)] += 1;
    }
}

card[9] = Math.ceil(card[9] / 2);

const maxValue = Math.max(...card);

console.log(maxValue);