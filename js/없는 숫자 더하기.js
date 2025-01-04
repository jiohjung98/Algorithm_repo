// function solution(numbers) {
//     var ans = 0;
//     for (i=0; i<10; i++) {
//         if (!numbers.includes(i)) {
//             ans += i;
//         }
//     }
//     return ans;
// }

// reduce 사용
function solution(numbers) {
    return 45 - numbers.reduce((cur, acc) => cur + acc, 0);
}