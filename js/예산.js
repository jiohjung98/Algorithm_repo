function solution(d, budget) {
    let tmp = 0;
    var answer = 0;
    let arr = d.sort((a,b) => a-b);

    for (let i=0; i < arr.length; i++) {
        tmp += arr[i]
        if (tmp > budget) {
            return answer
        } else {
            answer += 1
        }
    }
    return answer;
}