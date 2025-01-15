function solution(s) {
    var answer = 0;
    var cnt1 = 0;
    var cnt2 = 0;
    
    for (let i=0; i<s.length; i++) {
        if (cnt1 === cnt2) {
            answer += 1;
            var k = s[i];
        }
        
        if (k === s[i]) {
            cnt1 += 1;
        }
        else {
            cnt2 += 1;
        }
    }
    return answer;
}