function solution(cacheSize, cities) {
    if (cacheSize === 0) {
        return 5 * cities.length;
    }
    
    let answer = 0;
    let arr = [];
    
    for (city of cities) {
        city = city.toLowerCase();
        
        let idx = arr.indexOf(city);
        
        // index가 -1 : 배열 내에 원소가 없음
        // 따라서 -1보다 크면 배열 내에 원소가 있음을 의미
        if (idx > -1) {
            arr.splice(idx, 1);
            answer += 1;
        } else {
            if (arr.length >= cacheSize) {
                // arr길이가 cacheSize보다 크거나 같으면 마지막 원소 제거
                arr.shift();
            }
            answer += 5;
        }
        arr.push(city);
    }
    return answer;
}