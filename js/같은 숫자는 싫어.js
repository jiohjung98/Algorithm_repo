function solution(arr) {
    answer = [];
    answer.push(arr[0]);
    for (i=1; i<arr.length; i++) {
        if (answer[answer.length-1] !== arr[i]) {
            answer.push(arr[i]);
        }
    }
    return answer;
}