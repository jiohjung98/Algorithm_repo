function solution(n) {
    var answer = 0;
    for (i=1; i<=n/2; i++) {
        if (n % i == 0) {
            answer += 1
        }
    }
    
    return answer*2;
}

solution(20);
