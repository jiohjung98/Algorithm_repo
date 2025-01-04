// 내 풀이
// function solution(seoul) {
//     let ans = 0;
//     for (i=0; i<seoul.length; i++) {
//         if (seoul[i] === 'Kim') {
//             ans += i;
//         }
//     }
//     return '김서방은 ' + ans + '에 있다';
// }

// 더 좋은 풀이(indexOf 사용)
function solution(seoul) {
    let idx = seoul.indexOf('Kim');
    return '김서방은 ' + idx + '에 있다';
}