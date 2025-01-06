function solution(s) {
    var answer = [];
    var dic = {};
    for (let i=0; i<s.length; i++) {
        if (s[i] in dic) {
            answer.push(i-dic[s[i]]);
        } else {
            answer.push(-1);
        }
        dic[s[i]] = i;
    }
    return answer;
}