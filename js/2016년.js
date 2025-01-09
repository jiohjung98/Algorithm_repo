function solution(a, b) {
    const days = ['THU', 'FRI', 'SAT','SUN', 'MON', 'TUE','WED'];
    const months = [31,29,31,30,31,30, 31, 31, 30, 31, 30, 31];
    
    // reduce 초기값 0으로 설정 안하면 런타임 에러가 나는 이유
    // 만약 조건에 해당하는 월이 없을 경우(a가 1월일 때),
    // 빈 배열에서 reduce 메서드를 실행하기 때문에
    const answer = days[(months.filter((_,index) => index < a-1)
                    .reduce((acc,cur) => acc + cur, 0) + b) % 7];
        
    return answer;
}