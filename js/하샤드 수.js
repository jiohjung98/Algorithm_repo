function solution(x) {
    let arr = [...(x+'')];
    let sum = 0;
    arr.forEach(nums => {
        sum += parseInt(nums);
    })
    return x % sum === 0 ? true : false;
}