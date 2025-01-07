function solution(n) {
    let answer = n.toString(3);
    answer = [...answer].reverse().join('');
    return parseInt(answer, 3);
}