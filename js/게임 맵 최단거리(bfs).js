function solution(maps) {
    // 우, 하, 좌,
    const dx = [0, 1, 0, -1];
    const dy = [1, 0, -1, 0];
    
    const queue = [[0,0]];
    
    while (queue.length) {
        const [x,y] = queue.shift();
        
        for (let i=0; i<4; i++) {
            var nx = x + dx[i];
            var ny = y + dy[i];
            
            if (nx >= 0 && nx < maps.length && ny >= 0 && ny < maps[0].length && maps[nx][ny] === 1) {
                maps[nx][ny] = maps[x][y] + 1;
                queue.push([nx,ny]);
            }
        }
    }
    
    const answer = maps[maps.length-1][maps[0].length-1];
    
    return answer === 1 ? -1 : answer;
}