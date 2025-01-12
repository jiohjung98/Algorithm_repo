function solution(k, m, score) {
    var answer = 0;
    var arr = [];
    score.sort((a,b) => b-a);
    for (let i=0; i<score.length; i+=m) {
        arr.push(score.slice(i, i+m));
    }
    for (let j=0; j<arr.length; j++) {
        if(m === arr[j].length) {
            answer += Math.min(...arr[j]) * m;       
        }
    }
    return answer;
}