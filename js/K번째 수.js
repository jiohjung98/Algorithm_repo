function solution(array, commands) {
    const answer = []
    for (let a=0; a<commands.length; a++) {
        let i = commands[a][0];
        let j = commands[a][1];
        let k = commands[a][2];
        let new_arr = array.slice(i-1,j).sort((a,b) => a-b);
        answer.push(new_arr[k-1]);
    }
    return answer;
}