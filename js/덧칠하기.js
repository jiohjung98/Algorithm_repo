function solution(n, m, section) {
    var answer = 1;
    var paint = section[0];
    for (let i=0; i<section.length; i++) {
        if (section[i] - paint >= m) {
            answer += 1;
            paint = section[i];
        }
    }
    return answer;
}