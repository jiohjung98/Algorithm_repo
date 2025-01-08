function solution(strings, n) {
    return strings.sort((a,b) => {
        if (a[n] != b[n]) {
            // a[n]이 b[n]보다 크면 a[n]이 b[n]의 뒤에 옴
            return a[n] > b[n] ? 1 : -1;
        }
        return a > b ? 1 : -1;
    })
}

// sort
// 1 반환: 첫 번째 요소 a가 두 번째 요소 b 뒤로 이동.
// -1 반환: 첫 번째 요소 a가 두 번째 요소 b 앞으로 이동.
// 0 반환: 순서 변경 없음.