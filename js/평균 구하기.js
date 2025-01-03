// function solution(arr) {
//     let ans = 0;
//     arr.forEach(nums => {
//         ans += nums;
//     });
//     return ans / arr.length;
// }

function solution(arr) {
    return arr.reduce((a,b) => a+b) / arr.length;
}