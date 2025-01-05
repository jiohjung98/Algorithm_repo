function solution(t, p) {
    let answer = 0;
    for (let i=0; i<= t.length -p.length; i++) {
        if (parseInt([...t].slice(i, i+p.length).join('')) <= parseInt(p)) {
            answer++;
        }
    }
    return answer;
}