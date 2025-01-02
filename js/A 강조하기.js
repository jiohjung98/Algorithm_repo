// function soluiton(myString) {
//     return ([...myString].map(v => v.toLowerCase())).map(v => v === 'a' ? v.toUpperCase() : v).join('');
// }


function solution(myString) {
    return myString.toLowerCase().replaceAll('a', 'A');
}