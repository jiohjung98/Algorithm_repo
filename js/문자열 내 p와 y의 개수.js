// function solution(s){
//     let p_cnt = 0;
//     let y_cnt = 0;
//     let arr = [...s];
//     for (i=0; i<arr.length; i++) {
//         if (arr[i] == 'p' || arr[i] == 'P') {
//             p_cnt += 1;
//         }
//         if (arr[i] == 'y' || arr[i] == 'Y') {
//             y_cnt += 1;
//         }
//     }
//     if (p_cnt == y_cnt) {
//         return true;
//     } else {
//         return false;
//     }
// }

function solution(s) {
    return s.toUpperCase().split('P').length == s.toUpperCase().split('Y').length;
}