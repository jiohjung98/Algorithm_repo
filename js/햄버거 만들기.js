function solution(ingredient) {
    var answer = 0;
    var stack = [];
    
    ingredient.forEach((element) => {
        stack.push(element)
        if (JSON.stringify(stack.slice(-4)) === JSON.stringify([1, 2, 3, 1])) {
            answer += 1
            for (let i = 0; i < 4; i++) {
                stack.pop()
            }
        }
    })
    
    return answer;
}