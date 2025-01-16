function solution(participant, completion) {
    participant.sort();
    completion.sort();
    
    // filter 중괄호 사용하면 return이 반드시 필요함
    const diff = participant.filter((v, i) => {
        return v !== completion[i];
    })
    
    // filter 중괄호 없이 작성 시, return 필요 없음
    // const diff = participant.filter((p, i) => p !== completion[i]);
    
    return diff[0];
}