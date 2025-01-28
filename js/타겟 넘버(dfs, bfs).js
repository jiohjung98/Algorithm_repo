// bfs
function solution(numbers, target) {
    var answer = 0;
    var leaves = [0];
    
    for (let number of numbers) {
        var tmpArr = [];
        for (let leaf of leaves) {
            tmpArr.push(leaf + number);
            tmpArr.push(leaf - number);
        }
        leaves = tmpArr;
    }
    var answer = leaves.filter(e => target === e).length;
    return answer;
}

// dfs
var answer = 0;

function dfs(numbers, target, current, index) {
    if (numbers.length === index) {
        if (current === target) {
            answer++;
        }
        return
    }
    
    dfs(numbers, target, current + numbers[index], index + 1);
    dfs(numbers, target, current - numbers[index], index + 1);
}

function solution(numbers, target) {
    dfs(numbers, target, 0, 0);
    return answer;
}