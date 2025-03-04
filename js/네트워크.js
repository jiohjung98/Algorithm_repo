function solution(n, computers) {
    var visited = Array.from({length: n}, () => false);
    
    let answer = 0;
    
    function dfs(v) {
        visited[v] = true;
        
        for (let i=0; i<n; i++) {
            if (!visited[i] && computers[v][i] === 1) {
                dfs(i);
            }
        }
    }
        
    for (let i=0; i<n; i++) {
        if (!visited[i]) {
            dfs(i);
            answer++;
        }
    }
    
    return answer;
}