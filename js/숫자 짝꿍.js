function solution(X, Y) {
    const yFreq = {};
    for (let char of Y) {
        yFreq[char] = (yFreq[char] || 0) + 1;
    }
    const newArr = [];
    for (let char of X) {
        if (yFreq[char] > 0) {
            newArr.push(char);
            yFreq[char]--;
        }
    }
    if (newArr.length === 0) return '-1';
    
    return newArr.sort((a,b) => b-a).join('')[0] === '0' ? '0' : newArr.sort((a,b) => b-a).join('');
}