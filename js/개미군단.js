// function solution(hp) {
//     let answer = 0;
//     let hp2 = hp;
    
//     answer += parseInt(hp2 / 5);
//     hp2 = hp2 % 5;
//     answer += parseInt(hp2 / 3);
//     hp2 = hp2 % 3;
//     answer += parseInt(hp2 / 1);
//     return answer;
// }

function solution(hp) {
    return Math.floor(hp/5) + Math.floor((hp%5)/3) + (hp%5)%3;
}