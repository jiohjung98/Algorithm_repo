// 방법 1
// function solution(my_string) {
//     var arr = ['a','e','i','o','u'];
//     var answer = [...my_string].filter(x => x != 'a' && x != 'e' && x != 'i' && x != 'o' && x != 'u');

//     return answer.join('');
// }

// 방법 2
// function solution(my_string) {
//     return [...my_string].filter(x => !['a','e','i','o','u'].includes(x)).join('');
// }

// 방법 3
function solution(my_string) {
    return my_string.replace(/[aeiou]/g, '');
}