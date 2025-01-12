function solution(n) {
    let num = new Set();
    
    for (let i=2; i<n+1; i++) {
        num.add(i);
    }
    
    for (let j=2; j*j<=n; j++) {
        if (num.has(j)) {
            for (let k=j*j; k <=n; k+=j) {
                num.delete(k);
            }
        }
    }
    
    return num.size;
}