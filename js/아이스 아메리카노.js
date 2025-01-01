// function solution(money) {
//     var answer = [];
//     let cnt = parseInt(money / 5500);
//     let tmp = money - (5500*cnt);
//     answer.push(cnt, tmp);
    
//     return answer;
// }

function solution(money) {
    return [Math.floor(money / 5500), money % 5500];
}