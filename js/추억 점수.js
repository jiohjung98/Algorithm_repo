function solution(name, yearning, photo) {
    var arr = [];
    for (let i=0; i<photo.length; i++) {
        let cnt = 0;
        for (let j=0; j<photo[i].length; j++) {
            if (name.includes(photo[i][j])) {
                    cnt += yearning[name.indexOf(photo[i][j])];
            }
        }
        arr.push(cnt);  
    }
    return arr;
}