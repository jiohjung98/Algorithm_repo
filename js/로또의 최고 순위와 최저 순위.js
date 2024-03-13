function solution(lottos, win_nums) {
    var answer = [];
    
    let zero_count = 0
    let same_count = 0
    
    lottos.forEach(number => {
        if (number === 0) {
            zero_count++
        }
        else if (win_nums.includes(number)) {
            same_count++
        }
    })
    
    var max_value = Math.min(6, 7-(same_count+zero_count))
    var min_value = Math.min(6, 7-same_count)
    
    answer.push(max_value)
    answer.push(min_value)

    return answer;
}