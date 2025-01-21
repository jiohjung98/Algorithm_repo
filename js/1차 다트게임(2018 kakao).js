function solution(dartResult) {
    const matches = dartResult.match(/(\d+)([SDT])([*#]?)/g);
    var arr = [];
    
    for (const m of matches) {
        // 정규식은 3개의 캡처 그룹(()로 감싸진 부분)을 가지고 있으므로, match는 다음과 같은 배열을 반환
        // ["전체 매칭된 문자열", "첫 번째 캡처 그룹", "두 번째 캡처 그룹", "세 번째 캡처 그룹"]
        // 전체 매칭된 문자열 (match[0])이 필요하지 않다면 다음과 같이 무시할 수 있음
        // [_, 숫자, 보너스, 옵션]
        var [_, point, bonus, option] = m.match(/(\d+)([SDT])([*#]?)/);
        point = parseInt(point);
        if (bonus === 'D') {
            point **= 2;
        } else if (bonus === 'T') {
            point **= 3;
        }
        
        if (option === '*') {
            if (arr) {
                arr[arr.length-1] *= 2;
            }
            point *= 2;
        } else if (option === '#') {
            point *= -1;
        }
        arr.push(point);
    }
    return arr.reduce((acc,cur) => acc+cur, 0);
}