// // 내 풀이
// function solution(phone_number) {
//     let arr = [...phone_number];
//     arr.splice(0, arr.length - 4, '*'.repeat(arr.length - 4));
//     return arr.join('');
// }


//  replace와 정규식, 긍정형 전방 탐색 사용
// \d: 숫자 하나를 나타냄
// (?=\d{4}): 긍정형 전방 탐색 - 특정 조건이 뒤따르는 패턴을 찾음
// \d{4}: 숫자 4개가 뒤따르는 경우를 찾음
function solution(phone_number) {
    return phone_number.replace(/\d(?=\d{4})/g, '*');
}