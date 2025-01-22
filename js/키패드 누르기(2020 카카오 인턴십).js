function solution(numbers, hand) {
    const arr = [[1,2,3], [4,5,6], [7,8,9], ['*',0,'#']];
    var start_left_x = 3;
    var start_left_y = 0;
    var start_right_x = 3;
    var start_right_y = 2;
    const result = [];
    
    for (n of numbers) {
        for (let i=0; i<arr.length; i++) {
            if (arr[i].includes(n)) {
                var x = arr.indexOf(arr[i]);
                var y = arr[i].indexOf(n);
                break;
            }
        }
        
        if (n === 1 || n === 4 || n === 7) {
            result.push('L');
            start_left_x = x;
            start_left_y = y;
        }
        else if (n === 3 || n === 6 || n === 9) {
            result.push('R');
            start_right_x = x;
            start_right_y = y;
        }
        else {
            if (Math.abs(start_left_x - x) + Math.abs(start_left_y - y) < Math.abs(start_right_x - x) + Math.abs(start_right_y - y)) {
                result.push('L');
                start_left_x = x;
                start_left_y = y;
            } else if (Math.abs(start_left_x - x) + Math.abs(start_left_y - y) > Math.abs(start_right_x - x) + Math.abs(start_right_y - y)) {
                result.push('R');
                start_right_x = x;
                start_right_y = y;
            } else {
                if (hand === 'left') {
                    result.push('L');
                    start_left_x = x;
                    start_left_y = y;
                } else {
                   result.push('R');
                    start_right_x = x;
                    start_right_y = y; 
                }
            }
        }
    }
    return result.join('');
}