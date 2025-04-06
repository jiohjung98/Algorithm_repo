const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const bingo = [];
for (let i=0; i<5; i++) {
    bingo.push(input[i].split(' ').map(Number));
}

const bingo_num = [];
for (let i=5; i<10; i++) {
    bingo_num.push(input[i].split(' ').map(Number));
}

const check = () => {
    let result = 0;
    let cnt = 0;

    // 가로 빙고 체크
    for (let i=0; i<5; i++) {
        cnt = 0;
        for (let j=0; j<5; j++) {
            if (bingo[i][j] === 0) {
                cnt += 1;
            }
        }
        if (cnt === 5) {
            result += 1;
        }
    }

    // 세로 빙고 체크
    for (let i=0; i<5; i++) {
        cnt = 0;
        for (let j=0; j<5; j++) {
            if (bingo[j][i] === 0) {
                cnt += 1;
            }
        }
        if (cnt === 5) {
            result += 1;
        }
    }

    // 대각선 빙고 체크(왼->오)
    cnt = 0;
    for (let i=0; i<5; i++) {
        if (bingo[i][i] === 0) {
            cnt += 1;
        }
    }
    if (cnt === 5) {
        result += 1;
    }

    // 대각선 빙고 체크(오->왼)
    cnt = 0;
    for (let i=0; i<5; i++) {
        if (bingo[i][4-i] === 0) {
            cnt += 1;
        }
    }
    if (cnt === 5) {
        result += 1;
    }
    
    return result;
}

const simulation = () => {
    let result = 0;
    let cnt = 0;

    for (let i=0; i<5; i++) {
        for (let j=0; j<5; j++) {
            let num = bingo_num[i][j]
            cnt++;
            for (let k=0; k<5; k++) {
                for (let w=0; w<5; w++) {
                    if (num === bingo[k][w]) {
                        bingo[k][w] = 0;
                    }
                }
            }
            result = check();
            if (result >= 3) {
                return cnt;
            }
        }
    }
}

console.log(simulation());