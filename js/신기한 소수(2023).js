const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const n = Number(input[0]);

function isPrime(n) {
    if (n < 2) return false;
    for (let i=2; i*i <= n; i++) {
        if (n % i === 0) {
            return false;
        }
    }
    return true;
}

const result = [];

function dfs(num) {
    if (num.toString().length === n) {
        result.push(num);
    }
    else {
        for (let i=0; i<10; i++) {
            let temp = num * 10 + i;
            if (isPrime(temp)) {
                dfs(temp);
            }
        }
    }
}

dfs(2);
dfs(3);
dfs(5);
dfs(7);

console.log(result.join('\n'));