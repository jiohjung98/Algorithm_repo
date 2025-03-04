function solution(x, y, n) {
    let answer = -1;
    
    const queue = [];
    queue.push([x, 0]);
    const visited = new Set();
    
    while (queue.length > 0) {
        const [value, cnt] = queue.shift();
        
        if (value === y) {
            answer = cnt;
            break;
        }
        
        if (value * 3 <= y && !visited.has(value * 3)) {
            visited.add(value * 3);
            queue.push([value * 3, cnt + 1]);
        }
        if (value * 2 <= y && !visited.has(value * 2)) {
            visited.add(value * 2);
            queue.push([value * 2, cnt + 1]);
        }
        if (value + n <= y && !visited.has(value + n)) {
            visited.add(value + n);
            queue.push([value + n, cnt + 1]);
        }
    }
    
    return answer;
}