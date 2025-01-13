function isPrime(n) {
    if (n < 2) {
        return false
    }
    for (let i=2; i <= parseInt(n**0.5); i++) {
        if (n % i === 0) {
            return false
        }
    }
    return true
}

function solution(nums) {
    arr = [];
    let cnt = 0;
    for (let i=0; i<nums.length; i++) {
        for (let j=i+1; j<nums.length; j++) {
            for (let k=j+1; k<nums.length; k++) {
                arr.push([nums[i], nums[j], nums[k]]);
            }
        }
    }
    for (let i=0; i<arr.length; i++) {
        let tmp = arr[i].reduce((acc,cur) => acc+cur, 0);
        if (isPrime(tmp)) {
            cnt += 1;
        }
    }
    return cnt;
}