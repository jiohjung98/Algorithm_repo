const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const [N, K] = input[0].split(' ').map(Number);
const arr = Array.from({length: N}, (_, i) => i+1);
var answer = [];
var num = 0;

for (let i=0; i < N; i++) {
    num += K-1;
    if (num >= arr.length) {
        num %= arr.length;
    }
    // 원소 꺼내기 - splice
    // splice는 기본적으로 배열 형태로 반환되므로 값만 꺼내고싶으면 [0] 붙여줘야 함!!
    answer.push(arr.splice(num,1)[0]);
}

console.log(`<${answer.join(', ')}>`);