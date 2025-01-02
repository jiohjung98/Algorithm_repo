function solution(strArr) {
    return [...strArr].map(v => 
        strArr.indexOf(v) % 2 === 0 ? v.toLowerCase() : v.toUpperCase());
}