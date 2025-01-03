// 유클리드 호제법 다시 공부하기

function getGcd(a, b) {
    if (b === 0) return a;
    return getGcd(b, a % b);
  }
  
  function solution(arr) {
    return arr.reduce((a, b) => (a * b) / getGcd(a, b));
  }