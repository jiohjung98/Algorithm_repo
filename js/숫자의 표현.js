// function solution(n) {
//     var answer = 0;
//     for (let i = 1; i <= n; i++) { 
//         var sum = 0;
//         for (let j = i; j <= n; j++) { 
//             sum += j;
//             if (sum === n) {
//                 answer++;
//                 break;
//             } else if (sum > n) {
//                 break;
//             }
//         }
//     }
//     return answer;
// }

function solution(n) {
    let answer = 0;

    for (let m = 1; m * (m - 1) / 2 < n; m++) {
        // n - m * (m - 1) / 2가 m으로 나누어떨어지면 가능
        if ((n - (m * (m - 1)) / 2) % m === 0) {
            answer++;
        }
    }

    return answer;
}