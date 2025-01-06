function solution(s, n) {
    const lower = "abcdefghijklmnopqrstuvwxyz";
    const upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    var arr = [];
    
    for (let i=0; i<s.length; i++) {
        if (s[i] == ' ') {
            arr.push(' ');
        }
        else {
            // 대문자일 때
            if (s[i] === s[i].toUpperCase()) {
                let new_idx = [...upper].indexOf(s[i]) + n;
                arr.push([...upper][new_idx % 26]);
            } else {
                let new_idx = [...lower].indexOf(s[i]) + n;
                arr.push([...lower][new_idx % 26]);
            }
        }
    }
    return arr.join('');
}