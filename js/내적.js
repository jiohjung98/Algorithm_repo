// 내 풀이
// function solution(a, b) {
//     let arr = [];
//     for (let i=0; i<a.length; i++) {
//         arr.push(a[i] * b[i]);
//     }
//     return arr.reduce((cur,acc) => cur + acc, 0);
// }

// 좋은 풀이: 인자에 _ 를 넣는 : 사용하지 않는 인자일 경우 넣음
function solution(a,b) {
    return a.reduce((acc, _, i) => acc += a[i] * b[i], 0);
}