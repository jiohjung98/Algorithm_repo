function solution(food) {
    var arr = [];
    for (let i=1; i<food.length; i++) {
        let cnt = Math.floor(food[i] / 2);
        for (let j=0; j<cnt; j++) {
            arr.push(i);
        }
    }
    // 주의사항: 그냥 arr.reverse()를 하게되면 arr자체가 뒤집어짐 -> 원본배열이 수정됨
    // reverse()의 영향을 받지 않기 위해 arr 배열을 복사한 뒤 사용해야 함!!(전개연산자 사용)
    var converted_arr = [...arr].reverse();
    return arr.join('') + '0' + converted_arr.join('');
}