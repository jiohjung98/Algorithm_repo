const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const [n, k] = input[0].split(' ').map(Number);

const arr = input.slice(1).map(line => line.split(' ').map(Number));

arr.sort((a,b) =>{
    if (b[1] !== a[1]) return b[1]-a[1];
    if (b[2] !== a[2]) return b[2]-a[2];
    return b[3]-a-[3];
})

const idx = arr.findIndex(item => item[0] === k);

for (let i=0; i<arr.length; i++) {
    const [, gold, silver, bronze] = arr[i];
    const [, kg, ks, kb] = arr[idx];

    if (gold === kg && silver === ks && bronze === kb) {
        console.log(i+1);
        break;
    }
}