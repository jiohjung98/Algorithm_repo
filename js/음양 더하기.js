// 내 풀이
// function solution(absolutes, signs) {
//     let answer = 0;
//     for (i=0; i<absolutes.length; i++) {
//         if (signs[i] == true) {
//             answer += absolutes[i];
//         } else {
//             answer -= absolutes[i];
//         }
//     }
//     return answer;
// }

// reduce 사용
function solution(absolutes, signs) {
    return absolutes.reduce((acc, val, i) => acc + (val * (signs[i] ? 1 : -1)), 0);
}