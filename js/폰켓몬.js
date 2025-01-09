// js set -> new Set()
// set 길이 -> .size

function solution(nums) {
    var max_cnt = parseInt(nums.length / 2);
    const new_arr = new Set(nums);

    return Math.min(max_cnt, new_arr.size);
}