function solution(n, arr1, arr2) {
    let answer =[]
    for (let i=0; i<n; i++) {
        let tmp = arr1[i] | arr2[i];
        let convert_val = tmp.toString(2);
        let plus_zero = n - convert_val.length;
        // if (convert_val.length < n) {
        //     for (let j=0; j<plus_zero; j++) {
        //         convert_val = '0' + convert_val;
        //     }
        // }
        convert_val = convert_val.padStart(n, '0');
        
        answer.push(convert_val);
    }

    return answer.map(v => v.replace(/1/g, '#').replace(/0/g, ' '));
}