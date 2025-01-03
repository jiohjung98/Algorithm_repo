function solution(a, b) {
    let ans = 0;
    x = Math.max(a,b);
    y = Math.min(a,b);
    for (i=y; i<= x; i++) {
        ans += i;
    }
    return ans;
}