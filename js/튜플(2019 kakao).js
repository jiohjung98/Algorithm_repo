// JSON.parse : 문자열 -> JS 객체로 변환
// let s = "{{2},{2,1},{2,1,3},{2,1,3,4}}";
// let newArr = s.replace(/{/g, '[').replace(/}/g, ']');
// console.log(newArr); // "[[2],[2,1],[2,1,3],[2,1,3,4]]" (문자열)

// console.log(newArr[0]); ->  "[" (문자열의 첫 번째 문자)

// let parsedArr = JSON.parse(newArr);
// console.log(parsedArr); -> [[2],[2,1],[2,1,3],[2,1,3,4]] (JavaScript 배열)

function solution(s) {
    var answer = [];
    let newArr = JSON.parse(s.replace(/{/g, '[').replace(/}/g, ']'));
    newArr.sort((a,b) => a.length - b.length);
    
    for (i of newArr) {
        for (j of i) {
            if (!answer.includes(j)) {
                answer.push(j);
            }
        }
    }
    return answer;
}