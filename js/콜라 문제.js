function solution(a, b, n) {
    var answer = 0;
    while (n >= a) {
        var new_bottles = parseInt(n / a) * b;
        var remain_bottles = n % a;
        answer += new_bottles;
        n = new_bottles + remain_bottles;
    }
    return answer;
}