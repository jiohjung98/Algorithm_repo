// 방법 1 : 효율성 터짐
// 모든 배열을 순회하므로 

// function solution(phone_book) {
//     phone_book.sort((a,b) => a-b);
    
//     for (let i=0; i<phone_book.length-1; i++) {
//         for (let j=i+1; j<phone_book.length; j++) {
//             if (phone_book[j].startsWith(phone_book[i])) {
//                 return false
//             }
//         }
//     }
//     return true;
// }


// 방법 2 
// sort((a,b) => a-b)가 아닌 단순 sort() => 문자열 기준으로 정렬하기 때문에 인접한 문자열들이 모이게 됨
// 따라서 배열을 두 번 돌 필요가 없이 인접 인덱스들만 확인하면 됨
function solution(phone_book) {
    phone_book.sort();
    
    for (let i=0; i<phone_book.length-1; i++) {
        if (phone_book[i+1].startsWith(phone_book[i])) {
            return false
        }
    }
    return true;
}


// 방법 3
// JS의 some() 메서드
// 배열의 요소를 순회하면서 콜백 함수가 true를 반환하는 요소가 있는지를 확인
// 첫 번째로 true를 반환하는 순간 순회를 멈추고 true를 반환
// 모든 요소가 false를 반환하면 false 반환
// some은 조건 만족 시 true를 반환하므로 !를 통해 값 변환

function solution(phone_book) {
    return !phone_book.sort().some((_,i) => {
        if (i === phone_book.length-1) return false;
        return phone_book[i+1].startsWith(phone_book[i]);
    });
}