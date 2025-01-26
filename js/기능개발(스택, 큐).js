function solution(progresses, speeds) {
    var arr = [];
    for (let i=0; i < progresses.length; i++) {
        if (arr.length === 0 || arr[arr.length-1][0] < Math.ceil((100-progresses[i])/speeds[i]))         {
            arr.push([Math.ceil((100-progresses[i])/speeds[i]), 1]);
        }
        else {
            arr[arr.length-1][1] += 1;
        }
    }
    const answer = arr.map((elem) => elem[1]);
    
    return answer;
}