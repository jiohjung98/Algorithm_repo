// js 배열 마지막 인덱스 사용 방법
// 1. arr.at(-1);
// 2. arr[arr.length-1];

function solution(numbers) {
    var arr = numbers.sort((a,b) => b-a);
    return Math.max(arr[0]*arr[1], arr.at(-1) * arr.at(-2));
}