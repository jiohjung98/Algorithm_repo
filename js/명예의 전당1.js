function solution(k, score) {
    var stack = [];
    var answer = [];
    for (let i=0; i<score.length; i++) {
        stack.push(score[i]);
        stack.sort((a,b) => b-a);
        if (stack.length === k+1) {
            console.log(stack.pop());
            stack.pop();
        }
        answer.push(stack[stack.length-1]);
    }
    return answer;
}