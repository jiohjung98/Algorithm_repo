function solution(left, right) {
    let arr = [];
    for (let i=left; i<=right; i++) {
        arr.push(i);
    }
    return arr.reduce((acc, cur) => acc + (Number.isInteger(Math.sqrt(cur)) ? -cur : cur), 0);
}

// function solution(left, right) {
//     let answer = 0;
//     for (let i=left; i <=right; i++) {
//         if (Number.isInteger(Math.sqrt(i))) {
//             answer -= i;
//         } else {
//             answer += i;
//         }
//     }
//     return answer;
// }