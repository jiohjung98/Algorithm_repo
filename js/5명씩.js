function solution(names) {
    let arr = [];
    for (i=0; i<names.length; i+=5) {
        arr.push(names[i]);
        
    }
    return arr;
}