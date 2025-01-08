// js 배열 마지막 원소 제거 - shift()

function solution(cards1, cards2, goal) {
    for (let i=0; i<goal.length; i++) {
        if (cards1.length > 0 && cards1[0] === goal[i]) {
            cards1.shift();
        }
        else if (cards2.length > 0 && cards2[0] === goal[i]) {
             cards2.shift();
        }
        else {
            return 'No';
        }
    }
    return 'Yes';
}