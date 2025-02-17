function solution(word) {
    const words = 'AEIOU';
    const words_list = [];
    
    function dfs(cnt, w) {
        if (cnt === 5) return;
        for (let i=0; i<5; i++) {
            words_list.push(w+words[i]);
            dfs(cnt+1, w+words[i]);
        }
    }
    dfs(0, '');
    return words_list.indexOf(word) + 1;
}