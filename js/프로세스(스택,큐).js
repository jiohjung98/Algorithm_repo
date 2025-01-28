function solution(priorities, location) {
    var queue = [];
    var answer = 0;
    priorities.forEach((v,i) => {
        queue.push([i,v]);
    })
    while(true) {
        var cur = queue.shift();
        if (queue.some((v) => v[1] > cur[1])) {
            queue.push(cur);
        }
        else {
            answer += 1;
            if (cur[0] === location) {
                return answer;
            }
        }
    }
}