function solution(number, limit, power) {
    var answer = 0;
    let arr = Array.from({length: number+1}, () => 0);
    
    // 약수 개수 배열
    for (let i=1; i<number+1; i++) {
        for (let j=i; j<number+1; j+=i) {
            arr[j] += 1;
        }
    }

    for (let i=1; i<arr.length; i++) {
        if (arr[i] <= limit) {
            answer += arr[i];    
        } else {
            answer += power;
        }
    }
    return answer;
}