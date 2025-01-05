function solution(s) {
    
    let arr = (s+'').split(' ');
    return arr.map((v) => [...v].map((cur, idx) => idx % 2 === 0 ? cur.toUpperCase() : cur.toLowerCase()).join('')).join(' ');
}