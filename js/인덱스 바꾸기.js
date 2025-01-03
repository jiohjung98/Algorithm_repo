// function solution(my_string, num1, num2) {
//     return my_string.slice(0, num1) + my_string[num2] + my_string.slice(num1+1, num2) + my_string[num1] + my_string.slice(num2+1);
// }


// 구조 분해 할당
function solution(my_string, num1, num2) {
    my_string = my_string.split('');
    [my_string[num1], my_string[num2]] = [my_string[num2], my_string[num1]];
    return my_string.join('');
}