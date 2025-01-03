function solution(n) {
    return n.toString().split('').reduce((acc, curr) => acc + parseInt(curr), 0);
}

// initial value를 0으로 지정하는 이유
// reduce의 initial value는 첫 acc의 값이다.
// 0을 넣어서 acc 초기값을 정수화해주는 것