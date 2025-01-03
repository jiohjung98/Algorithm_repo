// function solution(todo_list, finished) {
//     let arr = [];
//     for (i=0; i<=todo_list.length; i++) {
//         if (finished[i] == false) {
//             arr.push(todo_list[i]);
//         }
//     }
//     return arr;
// }

function solution(todo_list, finished) {
    let arr = []
    return todo_list.filter((e,i) => !finished[i]);
}