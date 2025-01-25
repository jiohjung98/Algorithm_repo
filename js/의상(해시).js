// 1.	초기값 obj = {} (빈 객체).
// 2.	첫 번째 아이템 ["hat", "headgear"]:
// •	t[1] = "headgear".
// •	obj["headgear"]가 없으므로 1로 초기화.
// •	결과: { "headgear": 1 }.
// 3.	두 번째 아이템 ["sunglasses", "eyewear"]:
// •	t[1] = "eyewear".
// •	obj["eyewear"]가 없으므로 1로 초기화.
// •	결과: { "headgear": 1, "eyewear": 1 }.
// 4.	세 번째 아이템 ["turban", "headgear"]:
// •	t[1] = "headgear".
// •	obj["headgear"]가 이미 있으므로 +1.
// •	결과: { "headgear": 2, "eyewear": 1 }.


function solution(clothes) {
    return Object.values(clothes.reduce((obj, t) => {
      obj[t[1]] = obj[t[1]] ? obj[t[1]] + 1 : 1;
      return obj;
    }, {})).reduce((a,b) => a * (b+1), 1)-1;
}