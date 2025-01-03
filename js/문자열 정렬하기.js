// 방법 1: filter 사용(시간 복잡도: O(n))
// function solution(my_string) {
//     return [...my_string]
//             .filter(v => !isNaN(v))
//             .map(v => parseInt(v))
//             .sort((a,b) => a-b);
// }

// 방법 2: 정규식 사용(시간 복잡도: O(nlogn))
function solution(my_string) {
    return my_string.match(/\d/g).map(v => parseInt(v)).sort((a,b) => a-b);
}
