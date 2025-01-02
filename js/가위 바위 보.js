// function solution(rsp) {
//     const arr = [...rsp];
//     let answer = [];
//     for (i=0; i<=arr.length; i++) {
//         if (arr[i] == '0') answer.push('5');
//         if (arr[i] == '2') answer.push('0');
//         if (arr[i] == '5') answer.push('2');
//     }
    
//     return answer.join('');
// }

function solution(rsp) {
    let arr = {
        2: 0,
        0: 5,
        5: 2
    }
    return [...rsp].map(v => arr[v]).join('');
}