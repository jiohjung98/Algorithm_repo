function solution(answers) {
    const pattern1 = [1,2,3,4,5];
    const pattern2 = [2,1,2,3,2,4,2,5];
    const pattern3 = [3,3,1,1,2,2,4,4,5,5];

    let score = [0,0,0];
    let result = [];
    
    for (let i=0; i<answers.length; i++) {
        if (answers[i] == pattern1[i % pattern1.length]) {
            score[0] += 1;
        } if (answers[i] == pattern2[i % pattern2.length]) {
            score[1] += 1;
        } if (answers[i] == pattern3[i % pattern3.length]) {
            score[2] += 1;
        }
    }
    
    // console.log(Math.max(score) => Nan)
    // 왜? - Math.max는 숫자값을 비교하는 함수
    // score은 배열이므로 배열 자체를 숫자로 변환하려 시도하기 때문
    // 해결 방법 - 전개연산자 사용
    // Math.max(...score) => 만약 score이 [1,2,3]이면 Math.max(1,2,3)으로 동작
    const maxScore = Math.max(...score);
    for (let i=0; i<score.length; i++) {
        if (score[i] == maxScore) {
            result.push(i+1);
        }
    }
    return result;
}