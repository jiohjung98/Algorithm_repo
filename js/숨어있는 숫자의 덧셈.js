// function solution(my_string) {
//     let arr = [...my_string];
//     let answer = 0;
//     for (i=0; i <= my_string.length; i++) {
//         if (Math.floor(arr[i])) {
//             answer += Math.floor(arr[i]);
//         }
//     }
//     return answer;
// }

function solution(my_string) {
    return [...my_string].reduce((sum, char) => {
        const num = Math.floor(char);
        return sum + (isNaN(num) ? 0 : num);
    }, 0);
}