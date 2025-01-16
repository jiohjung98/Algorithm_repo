// forEach는 중간에 break를 사용할 수 없음!!!!
// function solution(keymap, targets) {
//     var answer = [];
//     targets.forEach(target => {
//         var count = 0;
//         [...target].forEach(t => {
//             var flag = false;
//             var maxLen = 101;
//             keymap.forEach(key => {
//                 if (key.includes(t)) {
//                     maxLen = Math.min([...key].indexOf(t)+1, maxLen);
//                     flag = true;
//                 }
//             })
//             if (flag === false) {
//                 count = -1;
//             } else {
//                 count += maxLen;
//             }
//         })
//         answer.push(count);
//     })
//     return answer;
// }


// 중간에 탈주해야하는 경우에는 forEach대신 그냥 for loop 사용
// 원소안에 접근할 때 in이 아닌 of 사용
function solution(keymap, targets) {
    var answer = [];
    targets.forEach(target => {
        var count = 0;
        for (let t of target) {
            var flag = false;
            var minLen = 101;
            for (let key of keymap) {
                if ([...key].includes(t)) {
                    minLen = Math.min([...key].indexOf(t)+1, minLen);
                    flag = true;
                }
            }
            if (!flag) {
                count = -1;
                break;
            } else {
                count += minLen
            }
        }
        answer.push(count);
    })
    return answer;
}
