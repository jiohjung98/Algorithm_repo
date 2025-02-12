function solution(str1, str2) {
    // 길이 2인 문자열로 자르기
    function splitTwoAlpha(str) {
        const arr = [];
        str = str.toLowerCase();
        
        for (let i=0; i<str.length-1; i++) {
            const pairs = str[i] + str[i+1];
            if (/^[a-z]{2}/.test(pairs)) {
                arr.push(pairs);
            }
        }
        return arr;
    }
    
    // 빈도수 구하기
    function Frequency(arr) {
        const map = new Map();
        for (let items of arr) {
            map.set(items, (map.get(items) || 0) + 1);
        }
        return map;
    }
    
    // 교집합, 전체집합 구하기
    function getIntersectionAndUnion(map1, map2) {
        let intersection = 0;
        let union = 0;
        const allKeys = new Set([...map1.keys(), ...map2.keys()]);
        
        for (const key of allKeys) {
            const cnt1 = map1.get(key) || 0;
            const cnt2 = map2.get(key) || 0;
            intersection += Math.min(cnt1, cnt2);
            union += Math.max(cnt1, cnt2);
        }
        
        return {intersection, union};
    }
    
    const arr1 = splitTwoAlpha(str1);
    const arr2 = splitTwoAlpha(str2);
    const map1 = Frequency(arr1);
    const map2 = Frequency(arr2);
    
    const {intersection, union} = getIntersectionAndUnion(map1, map2);
    
    if (union === 0) {
        return 65536;
    }
    return Math.floor((intersection / union) * 65536);
    
}