// JavaScript의 Set은 객체를 직접 비교할 수 없기 때문에 문자열로 변환해서 저장해야 함
// set의 경우 length가 아닌 size 반환

function solution(dirs) {
    const dir = {'U': [1,0], 'D': [-1,0], 'R': [0,1], 'L': [0,-1]};
    const set = new Set();
    let y = 0;
    let x = 0;
    
    for (let d of dirs) {
        let [dy, dx] = dir[d];
        let ny = y + dy;
        let nx = x + dx;
        
        if (ny >= -5 && ny <=5 && nx >= -5 && nx <= 5) {
            set.add(`${ny}-${nx}, ${y}-${x}`);
            set.add(`${y}-${x}, ${ny}-${nx}`);
            y = ny;
            x = nx;
        }
    }
    
    return set.size / 2;
}