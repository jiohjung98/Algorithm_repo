const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const [n, m] = input[0].split(' ').map(Number);
const arr = [];
for (let i=1; i<=n; i++) {
    arr.push(input[i].split('').map(Number));
}

function findSquare(s) {
    for (let i=0; i<n-s+1; i++) {
        for (let j=0; j<m-s+1; j++) {
            if (arr[i][j] === arr[i + s - 1][j] &&
                arr[i][j] === arr[i + s - 1][j + s - 1] &&
                arr[i][j] === arr[i][j + s - 1]) {
                return true;
            }
        }
    }
    return false;
}

const minValue = Math.min(n, m);

for (let x = minValue; x >= 0; x--) {
    if (findSquare(x)) {
        console.log(x**2);
        break;
    }
}