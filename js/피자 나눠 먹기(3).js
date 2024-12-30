// function solution(slice, n) {
//     var tmp = slice;
//     let answer = 1;
//     while (slice*answer < n) {
//         answer += 1
//     }
//     return answer;
// }

function solution(slice, n) {
    return Math.ceil(n / slice);
}