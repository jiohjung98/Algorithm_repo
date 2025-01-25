function solution(n, left, right) {
    var answer =[];
    for (let i=left; i <= right; i++) {
        var x = parseInt(i / n);
        var y = parseInt(i % n);
        answer.push(Math.max(x,y)+1);
    }
    return answer;
}