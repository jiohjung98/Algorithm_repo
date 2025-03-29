const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const t = Number(input[0]);

let index = 1;

for (let i=0; i < t; i++) {
    let [n, m] = input[index].split(' ').map(Number);
    const data = input[index+1].split(' ').map(Number);

    index += 2;

    let result = 1;

    while (data.length > 0) {
        if (data[0] < Math.max(...data)) {
            data.push(data[0]);
            data.shift();
        } else {
            if (m === 0) break;
            data.shift();
            result+=1;
        }
        if (m > 0) {
            m = m -1;
        } else {
            m = data.length-1;
        }
    }

    console.log(result);
}